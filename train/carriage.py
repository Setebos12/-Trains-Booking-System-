from Routes.Routes import Routes


class Cariage:
    def __init__(self, id: str, routes: list[Routes], seats, weight) -> None:
        pass

    def book_seat_for_route(self, starting_station, destination_station, seat_id, time=None):
        pass

    def list_all_availabe_seats(self, starting_station, destination_station, seat_id, time=None):
        pass

    def get_all_booked(self):
        pass

    def set_current_station(self):
        pass

    def set_next_station(self):
        pass