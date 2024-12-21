from datetime import datetime


class NotDateTimeDatError(Exception):
    pass


class Route:
    def __init__(self, starting_station: str, destination_station: str, arrival_time, departure_time, distance):
        self.starting_station = starting_station
        self.destination_station = destination_station
        self.set_arrive_time_departure_time(arrival_time, departure_time)
        self.set_disctance(distance)

        self.booked_data = None

    def arrival_time(self):
        return self._arrival_time

    def departure_time(self):
        return self._departure_time

    def set_disctance(self, distance):
        if distance < 0:
            return ValueError
        self._distance = distance

    def distance(self):
        return self._distance

    def book_route(self, data):
        self.booked_data = data

    def is_booked(self) -> bool:
        return self.booked_data is not None

    def undo_book_route(self):
        self.booked_data = None

    def set_arrive_time_departure_time(self, arrival_time, departure_time):
        if type(arrival_time) is not datetime or type(departure_time) is not datetime:
            raise NotDateTimeDatError(("Both arrival_time and departure_time must be datetime objects."))
        if arrival_time < departure_time:
            raise ValueError("Arrival time cannot be earlier than departure time.")
        self._arrival_time = arrival_time
        self._departure_time = departure_time


