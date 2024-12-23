from Routes.Route import Route
from networkx import DiGraph, has_path, shortest_path, shortest_path_length


class SeatsinRouteBookedError(Exception):
    pass


class Routes:
    """Routes will be in nx graph
    each node of graph is station : data in node (departure_time, arrival_time)
    each edge is road : data is (distance, data_booked)
    """
    def __init__(self, routes_id, routes: list[Route]):
        self.routes_id = routes_id
        self.routes = DiGraph()
        for route in routes:
            self.routes.add_node(route.starting_station,
                                 departure_time=route.departure_time())

        for route in routes:
            self.routes.add_edge(route.starting_station,
                                 route.destination_station,
                                 weight=route.distance(),
                                 )
            self.routes.nodes[route.destination_station]["arrival_time"] = route.arrival_time()

    def check_if_route_exist(self, starting_station: str, destination_station: str) -> bool:
        return has_path(self.routes, starting_station, destination_station)

    def calculate_road(self, starting_station: str, destination_station: str) -> int:
        return shortest_path_length(
            self.routes,
            starting_station,
            destination_station,
            weight='weight'
        )

    def stations_between(self, starting_station: str, destination_station: str):
        return shortest_path(self.routes, starting_station, destination_station)

    def calculate_time(self, starting_station: str, destination_station: str):
        departtime = self.routes.nodes[starting_station]['departure_time']
        arrivetime = self.routes.nodes[destination_station]['arrival_time']
        return arrivetime-departtime

    def get_departure_time(self, station: str):
        return self.routes.nodes[station]['departure_time']


    def get_arrival_time(self, station: str):
        return self.routes.nodes[station]['arrival_time']


class CarriageRoutes(Routes):
    def __init__(self, routes_id, routes: Routes, seats_id):
        self.routes_id = routes_id
        self.routes = routes.routes.copy()
        seats_booked = {seat_id: None for seat_id in seats_id}

        self.seats_id = seats_id
        # self.routes.edges['seats'] = seats_booked

        for u, v in self.routes.edges:
            self.routes.edges[u, v]['seats'] = seats_booked.copy()

    def check_if_can_booked(self, starting_station: str, destination_station: str, id: str):
        if self.check_if_route_exist(starting_station, destination_station) is False:
            return False
        tuple_stations = self.make_station_between_to_stations(starting_station, destination_station)

        for begin_station, end_station in tuple_stations:
            if self.routes.edges[begin_station, end_station]['seats'][id] is not None:
                return False
        return True

    def list_booked_and_an_empy_seats(self, starting_station: str, destination_station: str):
        seats_values = set(self.seats_id.copy())
        booked_seats_id = set()
        tuple_stations = self.make_station_between_to_stations(starting_station, destination_station)

        for begin_station, end_station in tuple_stations:
            for id in self.seats_id:
                if self.routes.edges[begin_station, end_station]['seats'][id] is not None:
                    booked_seats_id.add(id)

        return set(seats_values - booked_seats_id), set(booked_seats_id)

    def booked_seats(self, starting_station: str, destination_station: str, id: str, data):
        if self.check_if_can_booked(starting_station, destination_station, id) is False:
            raise SeatsinRouteBookedError

        tuple_stations = self.make_station_between_to_stations(starting_station, destination_station)

        for begin_station, end_station in tuple_stations:
            self.routes.edges[begin_station, end_station]['seats'][id] = data

    def make_station_between_to_stations(self, starting_station: str, destination_station: str):
        stations = self.stations_between(starting_station, destination_station)
        tuple_stations = make_tuple_from_list(stations)
        return tuple_stations


def make_tuple_from_list(nums):
    return [(nums[index], nums[index+1]) for index in range(len(nums)-1)]
