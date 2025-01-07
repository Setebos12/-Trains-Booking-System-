from train.train import Train
from networkx import DiGraph, compose, has_path, all_simple_paths
from file_handle.train_files import read_all_trains, write_train_file
from user.user import get_all_users, User, write_user_file
from System.MonitorUser import MonitorUserSystem
from user.ticket import Ticket
from typing import Dict, List
from Routes.Routes import Routes
from datetime import timedelta, datetime


class InvalidStationError(Exception):
    pass


class RouteError(Exception):
    pass


class InvalidTrainId(Exception):
    pass


class InvalidUserId(Exception):
    pass


class System:
    def __init__(self) -> None:
        self.trains = self._load_trains()
        self.users = self._load_users()
        self.network = self._create_graph_from_trains()
        self.all_stations = set(self.network.nodes)

    def _load_trains(self) -> Dict:
        return {train.id: train for train in read_all_trains()}

    def _load_users(self) -> Dict:
        return {user.id: user for user in get_all_users()}

    def add_user(self, user_id: str) -> None:
        if user_id in self.users:
            raise InvalidUserId(f"User with ID {user_id} already exists.")
        user = User(user_id)
        self.users[user.id] = user
        self.write_user_file(user)

    def write_user_file(self, user: User) -> None:
        write_user_file(user)

    def write_train_file(self, train: Train) -> None:
        write_train_file(train)

    def get_user(self, user_id: str) -> User:
        if user_id not in self.users:
            raise InvalidUserId(f"User with ID {user_id} does not exist.")
        return self.users[user_id]

    def _create_graph_from_trains(self) -> DiGraph:
        graph = DiGraph()
        for train in self.trains.values():
            graph = add_train_to_system(graph, train)
        return graph

    def _validate_station(self, station: str) -> None:
        if station not in self.all_stations:
            raise InvalidStationError(f"Invalid station: {station}")

    def check_direct_connection(self, starting_station: str, destination_station: str, time=None) -> List:
        self._validate_station(starting_station)
        self._validate_station(destination_station)

        if not has_path(self.network, starting_station, destination_station):
            raise RouteError("No path exists between the stations.")

        departures = self.network.nodes[starting_station].get('departure', {}).copy()
        arrivals = self.network.nodes[destination_station].get('arrivals', {}).copy()

        if time:
            departures = {key: value for key, value in departures.items() if value > time}

        common_keys = get_common(departures, arrivals)
        filtered_keys = common_keys.copy()

        for train_id in common_keys:
            route = self.get_train_route(train_id)
            if not route.check_if_route_exist(starting_station, destination_station):
                filtered_keys.remove(train_id)

        return sorted(filtered_keys, key=lambda train_id: departures[train_id])

    def check_no_direct_connections(
        self, starting_station: str, destination_station: str,
        time: datetime = None, time_wait: tuple = (0, 500)
    ) -> List:

        self._validate_station(starting_station)
        self._validate_station(destination_station)

        if not has_path(self.network, starting_station, destination_station):
            raise RouteError("No path exists between the stations.")

        paths = list(all_simple_paths(self.network, starting_station, destination_station))
        all_paths = []

        for path in paths:
            connections = self._find_connections_in_path(path, time, time_wait)
            all_paths.extend(connections)

        all_paths = list(set(all_paths))
        all_paths.sort(key=lambda path: path[3])  # Sort by transfer time
        return all_paths

    def _find_connections_in_path(self, path: List, time, time_wait) -> List:
        begin_station = path[0]
        end_station = path[-1]
        path_stations = set()

        for station in path[1:-1]:
            trains1 = self.check_direct_connection(begin_station, station, time)
            if not trains1:
                continue

            trains2 = self.check_direct_connection(station, end_station)
            if not trains2:
                continue

            for train1 in trains1:
                for train2 in trains2:
                    if train1 == train2:
                        continue
                    tran, tran_time = self.check_stations_correct_transfers(train1, train2, station, time_wait)
                    if tran:
                        path_stations.add((train1, train2, station, tran_time))

        return list(path_stations)

    def check_stations_correct_transfers(self, arrival_train: int,
                                         departure_train: int,
                                         station: str, time_wait: tuple = (0, 500)) -> tuple:
        arrival_time = self.network.nodes[station]['arrivals'][arrival_train]
        departure_time = self.network.nodes[station]['departure'][departure_train]
        time_diff = departure_time - arrival_time
        time_diff_minutes = time_diff.total_seconds() / 60

        if time_wait and not (time_wait[0] <= time_diff_minutes <= time_wait[1]):
            return 0, timedelta()

        return 1, time_diff

    def book_seat(self, starting_station: str, destination_station: str, train_id: int, route_id: int,
                  carriage_id: int, seat_id: int, user_id: str) -> None:
        if train_id not in self.trains:
            raise InvalidTrainId(f"Invalid train ID: {train_id}")

        if user_id not in self.users:
            raise InvalidUserId(f"Invalid user ID: {user_id}")

        train = self.trains[train_id]
        train.book_seat_for_route(starting_station, destination_station, carriage_id, seat_id, route_id, user_id)
        self.write_train_file(train)

        departure_time = train.routes[route_id].get_departure_time(starting_station)
        arrival_time = train.routes[route_id].get_arrival_time(destination_station)
        ticket = Ticket(starting_station, destination_station, train_id, route_id, carriage_id, seat_id,
                        departure_time, arrival_time)

        self.add_ticket_to_user(ticket, user_id)

    def add_ticket_to_user(self, ticket: Ticket, user_id: str) -> None:
        user = self.get_user(user_id)
        user.add_ticket(ticket)
        self.write_user_file(user)

    def remove_ticket(self, ticket: Ticket, user_id: str) -> None:
        user = self.get_user(user_id)
        user.remove_ticket(ticket)
        self.write_user_file(user)

        train = self.trains[ticket.train_id]
        train.book_seat_for_route(ticket.start_station, ticket.end_station, ticket.carriage_id, ticket.seat_id,
                                  ticket.route_id, None)
        self.write_train_file(train)

    def list_all_available_seats(self, starting_station: str, destination_station: str, route_id: int,
                                 train_id: int, r_data: Dict = None) -> Dict:
        if r_data is None:
            r_data = {}
        return self.trains[train_id].list_all_availabe_seats(starting_station, destination_station, route_id, r_data)

    def get_train_route(self, ids: tuple) -> Routes:
        route_id, train_id = ids
        return self.trains[train_id].routes[route_id]


class UserSystem:
    def __init__(self, system: System) -> None:
        self.system = system
        self.monitor_user = MonitorUserSystem("0")
        self.change_current_user("0")

    def change_current_user(self, user_id: str) -> None:
        if user_id not in self.system.users:
            self.system.add_user(user_id)
        self.monitor_user.user_id = user_id

    def book_seat_data(self) -> None:
        if not self.monitor_user or not self.monitor_user.check_if_all_not_none():
            raise ValueError("Incomplete booking data.")

        user_id = self.monitor_user.user_id
        starting_station = self.monitor_user.deparute
        destination_station = self.monitor_user.arrival
        train_id = self.monitor_user.train_id
        route_id = self.monitor_user.route_id
        carriage_id = self.monitor_user.carriage_id
        seat_id = self.monitor_user.seat_id

        self.system.book_seat(starting_station, destination_station, train_id, route_id, carriage_id, seat_id, user_id)


def get_common(nums1, nums2):
    return set(nums1) & set(nums2)


def merge_Graphs(G: DiGraph, grap_routes: DiGraph, train_id: int, route_id: int) -> DiGraph:
    graph = grap_routes.copy()
    data_nodes = dict(grap_routes.nodes(data=True))
    for node in graph.nodes:
        graph.nodes[node].clear()

    merger_graph = compose(G, graph)
    for node in data_nodes:
        if 'arrivals' not in merger_graph.nodes[node]:
            merger_graph.nodes[node]['arrivals'] = {}
        if 'departure' not in merger_graph.nodes[node]:
            merger_graph.nodes[node]['departure'] = {}

        if 'arrival_time' in data_nodes[node]:
            merger_graph.nodes[node]['arrivals'][(route_id, train_id)] = data_nodes[node]['arrival_time']
        if 'departure_time' in data_nodes[node]:
            merger_graph.nodes[node]['departure'][(route_id, train_id)] = data_nodes[node]['departure_time']
    return merger_graph


def add_train_to_system(G: DiGraph, train: Train) -> DiGraph:
    train_id = train.id
    for route in train.routes:
        G = merge_Graphs(G, train.routes[route].routes, train_id, route)
    return G
