from train.train import Train
from networkx import DiGraph, compose, has_path, all_simple_paths
from train.train_files import read_all_trains, write_train_file
from datetime import timedelta
from user.user import get_all_users, User, write_user_file
from System.MonitorUser import MonitorUserSystem
from user.ticket import Ticket
from train.train_files import read_all_trains

"""System Save data to files"""


class InvalidStationError(Exception):
    pass


class RouteError(Exception):
    pass


class System:
    def __init__(self):
        trains = read_all_trains()
        self.trains = {train.id: train for train in trains}
        self.create_graph_from_trains()
        self.all_stations = self.network.nodes.keys()
        list_user = get_all_users()
        self.users = {user.id: user for user in list_user}
        self.monitor_user = MonitorUserSystem(0)
        self.change_current_user(0)

    def add_user(self, user_id):
        user = User(user_id)
        if user.id in self.users.keys():
            raise ValueError
        self.users[user.id] = user
        write_user_file(user)
        self.monitor_user.user_id = user_id

    def change_current_user(self, user_id):
        if user_id not in self.users.keys():
            self.add_user(user_id)
        self.monitor_user.user_id = user_id

    def create_graph_from_trains(self):
        trains = read_all_trains()
        graph = DiGraph()
        for train in trains:
            graph = add_train_to_system(graph, train)
        self.network = graph

    def check_direct_connection(self, starting_station, destination_station, time=None):

        if starting_station not in self.all_stations or destination_station not in self.all_stations:
            raise InvalidStationError("Invalid starting or destination station.")

        if not has_path(self.network, starting_station, destination_station):
            raise RouteError("No path exists between the stations.")

        start_departures = self.network.nodes[starting_station]['departure'].copy()
        filtered_dict = start_departures

        if time is not None:
            filtered_dict = {key: value for key, value in start_departures.items() if value > time}

        destin_arrival = self.network.nodes[destination_station]['arrivals'].copy()

        common_keys = get_common(filtered_dict, destin_arrival)
        filtered_keys = common_keys.copy()

        for train_id in common_keys:
            route = self.get_train_route(train_id)
            if not route.check_if_route_exist(starting_station, destination_station):
                filtered_keys.remove(train_id)
        sorted_keys = sorted(
            filtered_keys,
            key=lambda train_id: filtered_dict[train_id]
        )

        return list(sorted_keys)

    def sort_keys(self, keys ,station):
        list_of_trains = []
        self.network.nodes[station]['departure']

    def check_no_direct_connections(self, starting_station, destination_station, time=None, time_wait=None):
        if has_path(self.network, starting_station, destination_station) is False:
            raise RouteError("No path exists between the stations.")

        paths = list(all_simple_paths(self.network, starting_station, destination_station))
        all_paths = []
        for path in paths:
            begin_station = path[0]
            end_station = path[-1]
            path_stations = set()
            for station in path[1:-1]:
                trains1 = self.check_direct_connection(begin_station, station, time)
                if trains1 == []:
                    continue
                trains2 = self.check_direct_connection(station, end_station)
                if trains2 == []:
                    continue
                for train1 in trains1:
                    for train2 in trains2:
                        if train1 == train2:
                            continue
                        tran, tran_time = self.check_stations_correct_transfers(train1, train2, station)
                        if time_wait:
                            if not time_wait[0] < tran_time < time_wait[1]:
                                continue
                        if tran == 1:
                            one_path = (train1,
                                        train2,
                                        station,
                                        tran_time)

                            path_stations.add(one_path)

            all_paths.extend(path_stations)
        return set(all_paths)

    def check_stations_correct_transfers(self, arrival_train, departure_train, station, transfer_tim=0):
        arrival_time = self.network.nodes[station]['arrivals'][arrival_train]
        deparute_time = self.network.nodes[station]['departure'][departure_train]
        time_diff = deparute_time - arrival_time
        time_diff_minutes = time_diff.total_seconds() / 60
        if time_diff_minutes < transfer_tim:
            return 0, 0

        return 1, deparute_time - arrival_time

    def book_seat(self, starting_station, destination_station, train_id, route_id ,carriage_id, seat_id, data):
        if train_id not in self.trains.keys():
            raise ValueError

        self.trains[train_id].book_seat_for_route(starting_station,
                                                  destination_station,
                                                  carriage_id,
                                                  seat_id,
                                                  route_id,
                                                  data)
        write_train_file(self.trains[train_id])

    def remove_ticket(self, ticket: Ticket):
        user_id = self.monitor_user.user_id
        starting_station = ticket.start_station
        destination_station = ticket.end_station
        train_id = ticket.train_id
        route_id = ticket.route_id
        carriage_id = ticket.carriage_id
        seat_id = ticket.seat_id
        self.book_seat(starting_station, destination_station, train_id, route_id, carriage_id, seat_id, None)
        self.users[user_id].remove_ticket(ticket)
        write_user_file(self.users[user_id])

    def book_seat_data(self):
        if not self.monitor_user:
            raise ValueError

        if not self.monitor_user.check_if_all_not_none():
            raise ValueError

        user_id = self.monitor_user.user_id
        starting_station = self.monitor_user.deparute
        destination_station = self.monitor_user.arrival
        train_id = self.monitor_user.train_id
        route_id = self.monitor_user.route_id
        carriage_id = self.monitor_user.carriage_id
        seat_id = self.monitor_user.seat_id
        self.book_seat(starting_station, destination_station, train_id, route_id, carriage_id, seat_id, user_id)
        departure_time = self.trains[train_id].routes[route_id].get_departure_time(starting_station)
        arrival_time = self.trains[train_id].routes[route_id].get_arrival_time(destination_station)
        ticket = Ticket(starting_station, destination_station, train_id, route_id, carriage_id, seat_id, departure_time, arrival_time)
        self.users[self.monitor_user.user_id].add_ticket(ticket)
        write_user_file(self.users[self.monitor_user.user_id])



    def list_all_availabe_seats(self, starting_station, destination_station, route_id, train_id, r_data={}):
        return self.trains[train_id].list_all_availabe_seats(starting_station, destination_station, route_id, r_data)

    def get_train_route(self, ids):
        route_id, train_id = ids
        route = self.trains[train_id].routes[route_id]
        return route

    def get_random_seat():
        pass


def get_common(nums1, nums2):
    return set(nums1) & set(nums2)


def merge_Graphs(G: DiGraph, grap_routes: DiGraph, train_id, route_id):

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


def add_train_to_system(G: DiGraph, train: Train):
    train_id = train.id
    for route in train.routes:
        G = merge_Graphs(G, train.routes[route].routes, train_id, route)
    return G
