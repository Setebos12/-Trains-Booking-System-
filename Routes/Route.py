from datetime import datetime


class NotDateTimeDatError(Exception):
    pass


class Route:
    def __init__(self, starting_station: str, destination_station: str,
                 arrival_time, departure_time, distance):
        self.starting_station = starting_station
        self.destination_station = destination_station
        self.set_arrive_time_departure_time(arrival_time, departure_time)
        self.set_distance(distance)
        self.booked_data = None

    def arrival_time(self):
        return self._arrival_time

    def departure_time(self):
        return self._departure_time

    def set_distance(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        self._distance = distance

    def distance(self):
        return self._distance

    def set_arrive_time_departure_time(self, arrival_time: datetime,
                                       departure_time: datetime):
        if not isinstance(arrival_time, datetime) or not isinstance(
                departure_time, datetime):
            raise NotDateTimeDatError(
                "Arrival_time and departure_time must be datetime objects.")
        if arrival_time < departure_time:
            raise ValueError(
                "Arrival time cannot be earlier than departure time.")
        self._arrival_time = arrival_time
        self._departure_time = departure_time
