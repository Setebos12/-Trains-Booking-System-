from Routes.Routes import CarriageRoutes, Routes
from train.Seats import Seat


class Cariage:
    def __init__(self, id: int, routes: list[Routes], seats: list[Seat],
                 carriage_look=None, initiation=True) -> None:
        self.id = id
        self.seats = {seat.data['id']: seat for seat in seats}
        self.seats_id = [seat.data['id'] for seat in self.seats.values()]

        if initiation:
            self._initialize(routes, carriage_look)
        else:
            self.routes = routes
            self.carriage_look = carriage_look

        self.current_route_id = 0

    def _initialize(self, routes: list[Routes], carriage_look=None):
        self.routes = {
            route.id: CarriageRoutes(route.id, route, self.seats_id) for route in routes
        }
        self.carriage_look = self.assign_seats(carriage_look) if carriage_look else None

    def book_seat_for_route(self, starting_station, destination_station,
                            seat_id, route_id, data):
        if route_id not in self.routes:
            raise ValueError

        self.routes[route_id].booked_seats(
            starting_station, destination_station, seat_id, data
        )

    def list_all_availabe_seats(self, starting_station, destination_station,
                                route_id, r_data={}):
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

    def assing_seats(self, carriage_look):
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

    def get_carriage_look(self, seats):
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

    def add_routes(self, route: Routes):
        self.routes[route.id] = CarriageRoutes(route.id, route, self.seats_id)

    def json_repr(self):
        return {
            'id': self.id,
            'seats': [seat.seat_repre() for seat in self.seats.values()],
            'carriage_look': self.carriage_look,
            'graph': {route.id: route.json_repr()
                      for route in self.routes.values()}
        }
