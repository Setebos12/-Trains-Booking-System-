from typing import List, Dict
from train.carriage import Cariage, json_repr_carriage
from Routes.Routes import Routes, json_repr_routes


class Train:
    def __init__(
        self, id: int, carriages: List[Cariage], routes: List[Routes]
    ) -> None:

        self.id = id
        self.carriages = {carriage.id: carriage for carriage in carriages}
        self.routes = {route.id: route for route in routes}

    def book_seat_for_route(
        self, starting_station: str, destination_station: str,
        carriage_id: int, seat_id: int, route_id: int, data: dict
    ) -> None:

        if carriage_id not in self.carriages:
            raise ValueError(f"Invalid carriage ID: {carriage_id}")
        self.carriages[carriage_id].book_seat_for_route(
            starting_station, destination_station, str(seat_id), route_id, data)

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

    def add_carriage(self, carriage: Cariage) -> None:
        if carriage.id in self.carriages:
            raise ValueError(f"Carriage with ID {carriage.id} already exists.")
        self.carriages[carriage.id] = carriage

    def remove_carriage(self, carriage_id: int) -> None:
        if carriage_id not in self.carriages:
            raise ValueError(f"Carriage with ID {carriage_id} does not exist.")
        del self.carriages[carriage_id]

    def __str__(self) -> str:
        return f"Train ID: {self.id}"


def json_repr_train(train: Train) -> Dict:
    return {
        'id': train.id,
        'carriages': {
            carriage.id: json_repr_carriage(carriage)
            for carriage in train.carriages.values()
        },
        'routes': {
            route.id: json_repr_routes(route) for route in train.routes.values()
        },
    }
