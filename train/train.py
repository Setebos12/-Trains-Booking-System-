from train.carriage import Cariage
from Routes.Routes import Routes


class Train:
    def __init__(self, id, carriages: list[Cariage], routes: list[Routes],
                 initiatin=True):
        self.id = id
        self.carriages = {carriage.id: carriage for carriage in carriages}
        self.routes = {route.id: route for route in routes}
        if initiatin is True:
            self.assign_routes_to_carriages()

    def book_seat_for_route(self, starting_station, destination_station,
                            carriage_id, seat_id, route_id, data):
        if carriage_id not in self.carriages.keys():
            raise ValueError
        seat_id = str(seat_id)
        self.carriages[carriage_id].book_seat_for_route(
            starting_station, destination_station, seat_id, route_id, data)

    def list_all_availabe_seats(self, starting_station, destination_station,
                                route_id, r_data={}):
        avalibe = {}
        for key in self.carriages:
            avalibe_seats = self.carriages[key].list_all_availabe_seats(
                starting_station, destination_station, route_id, r_data)
            avalibe[key] = avalibe_seats
        return avalibe

    def assign_routes_to_carriages(self):
        routes = self.routes.copy()
        for route in routes.values():
            for key in self.carriages:
                self.carriages[key].add_routes(route)

    def list_of_ids(self):
        return self.routes.keys()

    def json_repr(self):
        return {
            'id': self.id,
            'carrages': {carriage.id:
                         carriage.json_repr()
                         for carriage in self.carriages.values()},
            'routes': {route.id:
                       route.json_repr() for route in self.routes.values()}
        }

    def __str__(self):
        return f"{self.id}"
