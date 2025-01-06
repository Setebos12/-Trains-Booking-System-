class Ticket:
    def __init__(self, start_station, end_station, train_id, route_id,
                 carriage_id, seat_id, departure_time, arrival_time):
        self.start_station = start_station
        self.end_station = end_station
        self.train_id = train_id
        self.route_id = route_id
        self.carriage_id = carriage_id
        self.seat_id = seat_id
        self.arrival_time = str(arrival_time)
        self.departure_time = str(departure_time)

    def __str__(self):
        return (
            f"Ticket:\n"
            f"  Start Station: {self.start_station}\n"
            f"  Departure Time: {self.departure_time}\n"
            f"  End Station: {self.end_station}\n"
            f"  Arrival Time: {self.arrival_time}\n"
            f"  Train ID: {self.train_id}\n"
            f"  Route ID: {self.route_id}\n"
            f"  Carriage ID: {self.carriage_id}\n"
            f"  Seat ID: {self.seat_id}\n"


        )


def json_repr_ticket(ticket: Ticket):
    return {
        "start_station": ticket.start_station,
        "end_station": ticket.end_station,
        "train_id": ticket.train_id,
        "route_id": ticket.route_id,
        "carriage_id": ticket.carriage_id,
        "seat_id": ticket.seat_id,
        "arrival_time": ticket.arrival_time,
        "departure_time": ticket.departure_time,
    }