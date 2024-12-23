from Routes.Routes import CarriageRoutes, Routes
from train.Seats import Seat


class Cariage:
    def __init__(self, id: int, routes: list[Routes], seats: list[Seat], carriage_look=None) -> None:
        self.id = id
        self.seats = seats
        self.seats_id = [seat.data['id'] for seat in self.seats]
        self.routes = {route.routes_id: CarriageRoutes(route.routes_id, route, self.seats_id) for route in routes}
        if carriage_look is not None:
            self.carriage_look = self.assing_seats(carriage_look)
        else:
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

    def filter_seats(self, r_data):
        seats_id = set()
        for seat in self.seats:
            if seat.check_requirments(r_data):
                seats_id.add(seat.data['id'])
        return seats_id

    def assing_seats(self, carriage_look):
        seats_id = [seat.data['id'] for seat in self.seats]
        seats_id.sort()

        index = 0
        for x_dim in range(len(carriage_look)):
            for y_dim in range(len(carriage_look[x_dim])):
                if carriage_look[x_dim][y_dim] == 'S':
                    carriage_look[x_dim][y_dim] = str(carriage_look[x_dim][y_dim]) + str(seats_id[index])
                    index += 1
                    if index > len(seats_id):
                        return
        return carriage_look

    def get_carriage_look(self, seats):
        free_seat, booked_seats = seats
        carriage_look = self.carriage_look.copy()

        for x_dim in range(len(carriage_look)):
            for y_dim in range(len(carriage_look[x_dim])):
                if carriage_look[x_dim][y_dim][0] == 'S':
                    index = int(carriage_look[x_dim][y_dim][1:])
                    if index in free_seat:
                        carriage_look[x_dim][y_dim] += 'F'
                    else:
                        carriage_look[x_dim][y_dim] += 'B'
        return carriage_look

    def add_routes(self, route: Routes):
        self.routes[route.routes_id] = CarriageRoutes(route.routes_id, route, self.seats_id)

    def set_next_station(self):
        pass