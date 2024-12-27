class Ticket:
    def __init__(self, start_station, end_station, train_id, route_id, carriage_id, seat_id):
        self.start_station = start_station
        self.end_station = end_station
        self.train_id = train_id
        self.route_id = route_id
        self.carriage_id = carriage_id
        self.seat_id = seat_id

    def json_repr(self):
        return {
            "start_station": self.start_station,
            "end_station": self.end_station,
            "train_id": self.train_id,
            "route_id": self.route_id,
            "carriage_id": self.carriage_id,
            "seat_id": self.seat_id
        }

    def __str__(self):
        return (
            f"Ticket:\n"
            f"  Start Station: {self.start_station}\n"
            f"  End Station: {self.end_station}\n"
            f"  Train ID: {self.train_id}\n"
            f"  Route ID: {self.route_id}\n"
            f"  Carriage ID: {self.carriage_id}\n"
            f"  Seat ID: {self.seat_id}"
        )