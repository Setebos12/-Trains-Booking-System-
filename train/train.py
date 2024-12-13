from train.carriage import Cariage
from train.locomotive import Locomotive
from Routes.Routes import Routes


class Train:
    def __init__(self, carriages: list[Cariage], locomotives: list[Locomotive], routes: list[Routes]):
        pass

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

    def book_seat_for_route(self, starting_station, destination_station, carriage_id, seat_id, time=None):
        pass

    def list_all_availabe_seats(self, starting_station, destination_station, seat_id, time=None):
        pass