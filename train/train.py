from train.carriage import Cariage
from train.locomotive import Locomotive
from Routes.Routes import Routes


class Train:
    def __init__(self, carriages: list[Cariage], routes: list[Routes]):
        self.carriages = {carriage.id: carriage for carriage in carriages}
        self.routes = {route.routes_id: route for route in routes}
        self.assign_routes_to_carriages()

    def set_current_locomotive(self):
        pass

    def insert_carriage(self):
        pass

    def remove_carriage(self):
        pass

    def add_locomotive(self):
        pass

    def remove_locomotive(self):
        pass

    def book_seat_for_route(self, starting_station, destination_station, carriage_id, seat_id, route_id, data,time=None):
        if carriage_id not in self.carriages.keys():
            raise ValueError

        self.carriages[carriage_id].book_seat_for_route(starting_station, destination_station, seat_id, route_id, data)

    def list_all_availabe_seats(self, starting_station, destination_station, route_id, time=None):
        avalibe = {}
        for key in self.carriages:
            avalibe_seats = self.carriages[key].list_all_availabe_seats(starting_station, destination_station, route_id)
            avalibe[key] = avalibe_seats
        return avalibe

    def assign_routes_to_carriages(self):
        routes = self.routes.copy()
        for route in routes.values():
            for key in self.carriages:
                self.carriages[key].add_routes(route)

"""Do list Seat with requriments"""