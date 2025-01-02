from typing import List, Dict
from Routes.Routes import CarriageRoutes, Routes
from train.Seats import Seat


class Cariage:
    def __init__(
        self, id: int, routes: List[Routes], seats: List[Seat],
        carriage_look: List[List[str]] = None, initiation: bool = True
    ) -> None:
        self.id = id
        self.seats = {seat.data['id']: seat for seat in seats}
        self.seats_id = [seat.data['id'] for seat in self.seats.values()]

        if initiation:
            self._initialize(routes, carriage_look)
        else:
            self.routes = routes
            self.carriage_look = carriage_look

        self.current_route_id = 0

    def _initialize(
        self, routes: List[Routes], carriage_look: List[List[str]] = None
    ) -> None:
        self.routes = {
            route.id: CarriageRoutes(route.id, route, self.seats_id) for route in routes
        }
        self.carriage_look = self.assign_seats(carriage_look) if carriage_look else None

    def book_seat_for_route(
        self, starting_station: str, destination_station: str,
        seat_id: str, route_id: int, data: Dict
    ) -> None:
        """
        Books a seat for a specific route.

        Args:
            starting_station (str): Starting station.
            destination_station (str): Destination station.
            seat_id (str): Seat ID.
            route_id (int): Route ID.
            data (dict): Booking data.

        Raises:
            ValueError: If the route ID is invalid.
        """
        if route_id not in self.routes:
            raise ValueError

        self.routes[route_id].booked_seats(
            starting_station, destination_station, seat_id, data
        )

    def list_all_available_seats(
        self, starting_station: str, destination_station: str,
        route_id: int, r_data: Dict = None
    ) -> tuple:
        """
        Lists all available seats for a given route and station range.

        Args:
            starting_station (str): Starting station.
            destination_station (str): Destination station.
            route_id (int): ID of the route.
            r_data (dict, optional): Seat requirement filters. Defaults to None.

        Returns:
            tuple: (set of free seats, set of booked seats)
        """
        if route_id not in self.routes:
            raise ValueError
        free_s, book_s = self.routes[route_id].list_booked_and_empty_seats(
            starting_station, destination_station)
        seats_id = self.filter_seats(r_data)
        free_s = set(free_s) & set(seats_id)
        return free_s, book_s

    def filter_seats(self, r_data):
        return {
            seat.data['id'] for seat in self.seats.values()
            if seat.check_requirments(r_data)
        }

    def assign_seats(self, carriage_look: List[List[str]]) -> List[List[str]]:
        seats_id = self.seats_id
        seats_id.sort(key=int)
        index = 0
        for x_dim, row in enumerate(carriage_look):
            for y_dim, cell in enumerate(row):
                if cell == 'S':
                    if index >= len(seats_id):
                        return carriage_look
                    carriage_look[x_dim][y_dim] = f"S{seats_id[index]}"
                    index += 1
        return carriage_look

    def get_carriage_look(self, seats: tuple) -> List[List[str]]:
        """
        Returns the visual representation of the carriage layout.

        Args:
            seats (tuple): (set of free seats, set of booked seats).

        Returns:
            List[List[str]]: Visual layout with seat statuses.
        """
        free_seats, booked_seats = seats
        layout = []
        for row in self.carriage_look:
            new_row = []
            for cell in row:
                if cell[0] == 'S':
                    seat_id = cell[1:]
                    if seat_id in free_seats:
                        new_row.append(f"{cell}F")
                    elif seat_id in booked_seats:
                        new_row.append(f"{cell}B")
                    else:
                        new_row.append(cell)
                else:
                    new_row.append(cell)
            layout.append(new_row)
        return layout

    def add_routes(self, route: Routes) -> None:
        self.routes[route.id] = CarriageRoutes(route.id, route, self.seats_id)

    def json_repr(self) -> Dict:
        return {
            'id': self.id,
            'seats': [seat.seat_repr() for seat in self.seats.values()],
            'carriage_look': self.carriage_look,
            'graph': {route.id: route.json_repr()
                      for route in self.routes.values()}
        }
