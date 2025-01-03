from typing import List, Dict
from train.carriage import Cariage
from Routes.Routes import Routes


class Train:
    def __init__(
        self, id: int, carriages: List[Cariage], routes: List[Routes],
        initiating: bool = True
    ) -> None:

        self.id = id
        self.carriages = {carriage.id: carriage for carriage in carriages}
        self.routes = {route.id: route for route in routes}
        if initiating:
            self.assign_routes_to_carriages()

    def book_seat_for_route(
        self, starting_station: str, destination_station: str,
        carriage_id: int, seat_id: int, route_id: int, data: dict
    ) -> None:

        if carriage_id not in self.carriages:
            raise ValueError(f"Invalid carriage ID: {carriage_id}")
        self.carriages[carriage_id].book_seat_for_route(
            starting_station, destination_station, str(seat_id), route_id, data
        )

    def list_all_available_seats(
        self, starting_station: str, destination_station: str,
        route_id: int, r_data: dict = None
    ) -> Dict[int, List[str]]:

        if r_data is None:
            r_data = {}
        available = {}
        for carriage_id, carriage in self.carriages.items():
            available_seats = carriage.list_all_available_seats(
                starting_station, destination_station, route_id, r_data
            )
            available[carriage_id] = available_seats
        return available

    def assign_routes_to_carriages(self) -> None:
        for route in self.routes.values():
            for carriage in self.carriages.values():
                carriage.add_routes(route)

    def list_of_ids(self) -> List[int]:
        return list(self.routes.keys())

    def json_repr(self) -> Dict:
        return {
            'id': self.id,
            'carriages': {
                carriage.id: carriage.json_repr()
                for carriage in self.carriages.values()
            },
            'routes': {
                route.id: route.json_repr() for route in self.routes.values()
            },
        }

    def __str__(self) -> str:
        return f"Train ID: {self.id}"
