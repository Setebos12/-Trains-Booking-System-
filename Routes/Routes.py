from Routes.Route import Route
from networkx import DiGraph, has_path, shortest_path, shortest_path_length
from networkx.readwrite.json_graph import node_link_data
from datetime import datetime
from typing import List


class SeatsinRouteBookedError(Exception):
    pass


def create_graph_from_routes(routes: list[Route]) -> DiGraph:
    DiGroutes = DiGraph()
    for route in routes:
        DiGroutes.add_node(
            route.starting_station,
            departure_time=route.departure_time(),
        )

    for route in routes:
        DiGroutes.add_edge(
            route.starting_station,
            route.destination_station,
            weight=route.distance(),
        )
        DiGroutes.nodes[route.destination_station]["arrival_time"] = (
            route.arrival_time()
        )
    return DiGroutes


class Routes:
    """Routes will be in nx graph.
    Each node of graph is a station: data in node (departure_time, arrival_time).
    Each edge is a road: data is (distance, data_booked).
    """
    def __init__(self, id, routes: DiGraph, create_graph=True) -> None:
        self.id = id
        self.routes = routes

    def check_if_route_exist(self, starting_station: str, destination_station: str) -> bool:
        return has_path(self.routes, starting_station, destination_station)

    def calculate_road(self, starting_station: str, destination_station: str) -> int:
        return shortest_path_length(
            self.routes,
            starting_station,
            destination_station,
            weight='weight'
        )

    def stations_between(self, starting_station: str, destination_station: str) -> List[str]:
        return shortest_path(self.routes, starting_station, destination_station)

    def calculate_time(self, starting_station: str, destination_station: str) -> int:
        depart_time = self.routes.nodes[starting_station]['departure_time']
        arrive_time = self.routes.nodes[destination_station]['arrival_time']
        return arrive_time - depart_time

    def get_departure_time(self, station: str) -> datetime:
        return self.routes.nodes[station]['departure_time']

    def get_arrival_time(self, station: str) -> datetime:
        return self.routes.nodes[station]['arrival_time']

    def info_route(self, starting_station: str, destination_station: str):
        departure_time = self.get_departure_time(starting_station)
        arrival_time = self.get_arrival_time(destination_station)
        route_distance = self.calculate_road(starting_station, destination_station)
        travel_time = self.calculate_time(starting_station, destination_station)
        return (
            str(departure_time)[:-3],
            str(arrival_time)[:-3],
            f"{float(route_distance):.2f} km",
            f"Journey time {str(travel_time)[:-3]}"
        )


def json_repr_routes(routes: Routes):
    return {
        'id': routes.id,
        'graph': node_link_data(routes.routes, edges="edges")
    }


class CarriageRoutes(Routes):
    def __init__(self, id: int, routes: DiGraph, seats_id: List[int], initation: bool = True) -> None:
        self.id = id
        if initation:
            self._initialize(routes, seats_id)
        else:
            self.routes = routes
            self.seats_id = seats_id

    def _initialize(self, routes, seats_id):
        self.routes = routes.routes.copy()
        seats_booked = {str(seat_id): None for seat_id in seats_id}
        self.seats_id = seats_id

        for u, v in self.routes.edges:
            self.routes.edges[u, v]['seats'] = seats_booked.copy()

    def check_if_can_booked(self, starting_station: str, destination_station: str, seat_id: str) -> bool:
        if not self.check_if_route_exist(starting_station, destination_station):
            return False

        tuple_stations = self.make_station_between_to_stations(starting_station, destination_station)
        for begin_station, end_station in tuple_stations:
            if self.routes.edges[begin_station, end_station]['seats'][str(seat_id)] is not None:
                return False
        return True

    def list_booked_and_empty_seats(self, starting_station: str, destination_station: str) -> tuple:
        seats_values = set(self.seats_id)
        booked_seats_id = set()
        tuple_stations = self.make_station_between_to_stations(starting_station, destination_station)

        for begin_station, end_station in tuple_stations:
            for seat_id in self.seats_id:
                if self.routes.edges[begin_station, end_station]['seats'][str(seat_id)] is not None:
                    booked_seats_id.add(seat_id)
        return set(seats_values - booked_seats_id), set(booked_seats_id)

    def booked_seats(self, starting_station: str, destination_station: str, seat_id: str, data: any) -> None:
        if data is not None and not self.check_if_can_booked(starting_station, destination_station, seat_id):
            raise SeatsinRouteBookedError

        tuple_stations = self.make_station_between_to_stations(starting_station, destination_station)
        for begin_station, end_station in tuple_stations:
            self.routes.edges[begin_station, end_station]['seats'][seat_id] = data

    def make_station_between_to_stations(self, starting_station: str, destination_station: str) -> List[tuple]:
        stations = self.stations_between(starting_station, destination_station)
        return make_tuple_from_list(stations)


def make_tuple_from_list(nums):
    return [(nums[index], nums[index + 1]) for index in range(len(nums) - 1)]
