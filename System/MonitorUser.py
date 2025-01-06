class MonitorUserSystem():
    def __init__(self, user_id):
        self.user_id = user_id
        self.deparute = None
        self.arrival = None
        self.train_id = None
        self.route_id = None
        self.carriage_id = None
        self.seat_id = None

    def check_if_all_not_none(self):
        return all([
            self.deparute is not None,
            self.arrival is not None,
            self.train_id is not None,
            self.route_id is not None,
            self.carriage_id is not None,
            self.seat_id is not None,
        ])
