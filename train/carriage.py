from Routes.Routes import CarriageRoutes, Routes
from train.Seats import Seat


class Cariage:
    def __init__(self, id: int, routes: list[Routes], seats: list[Seat], carriage_look=None, initiation=True) -> None:
        self.id = id
        self.seats = {seat.data['id']: seat for seat in seats}
        self.seats_id = [seat.data['id'] for seat in self.seats.values()]

        if initiation is True:
            self.routes = {route.id: CarriageRoutes(route.id, route, self.seats_id) for route in routes}
            if carriage_look is not None:
                self.carriage_look = self.assing_seats(carriage_look)
            else:
                self.carriage_look = None
        else:
            self.routes = routes
            self.carriage_look = carriage_look

        self.current_route_id = 0

    def book_seat_for_route(self, starting_station, destination_station, seat_id, route_id, data, time=None):
        if route_id not in self.routes:
            raise ValueError

        self.routes[route_id].booked_seats(starting_station, destination_station, seat_id, data)

    def list_all_availabe_seats(self, starting_station, destination_station, route_id, r_data={}):
        if route_id not in self.routes:
            raise ValueError
        free_seats, booked_seats = self.routes[route_id].list_booked_and_an_empy_seats(starting_station, destination_station)
        seats_id = self.filter_seats(r_data)
        free_seats = set(free_seats) & set(seats_id)
        return free_seats, booked_seats

    def filter_seats(self, r_data):
        seats_id = set()
        for seat in self.seats.values():
            if seat.check_requirments(r_data):
                seats_id.add(seat.data['id'])
        return seats_id

    def assing_seats(self, carriage_look):
        seats_id = self.seats_id
        seats_id.sort(key=int)
        print(seats_id)
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
        carriage_look = []
        for x_dim in range(len(self.carriage_look)):
            row = []
            for y_dim in range(len(self.carriage_look[x_dim])):
                if self.carriage_look[x_dim][y_dim][0] == 'S':
                    index = int(self.carriage_look[x_dim][y_dim][1:3])
                    if str(index) in free_seat:
                        row.append(self.carriage_look[x_dim][y_dim] + 'F')
                    else:
                        row.append(self.carriage_look[x_dim][y_dim] + 'B')
                else:
                    row.append(self.carriage_look[x_dim][y_dim])
            carriage_look.append(row)

        return carriage_look

    def add_routes(self, route: Routes):
        self.routes[route.id] = CarriageRoutes(route.id, route, self.seats_id)

    def carriage_repr(self):
        return {
            'id': self.id,
            'seats': [seat.seat_repre() for seat in self.seats.values()],
            'carriage_look': self.carriage_look,
            'graph': {route.id: route.json_repr() for route in self.routes.values()}
        }
