from Routes.Routes import CarriageRoutes, Routes
from train.Seats import Seat


class Cariage:
    def __init__(self, id: int, routes: list[Routes], seats: list[Seat]) -> None:
        self.id = id
        self.seats = seats
        seats_id = [seat.data['id'] for seat in self.seats]
        self.routes = {route.routes_id :CarriageRoutes(route.routes_id, route, seats_id) for route in routes}
        self.carriage_look = None
        self.current_route_id = 0

    def book_seat_for_route(self, starting_station, destination_station, seat_id, route_id, data, time=None):
        if route_id not in self.routes:
            raise ValueError

        self.routes[route_id].booked_seats(starting_station, destination_station, seat_id, data)

    def list_all_availabe_seats(self, starting_station, destination_station, route_id, time=None):
        if route_id not in self.routes:
            raise ValueError
        return self.routes[route_id].list_booked_and_an_empy_seats(starting_station, destination_station)

    def get_all_booked(self):
        pass

    def set_current_station(self):
        pass

    def set_next_station(self):
        pass