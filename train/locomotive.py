from train.carriage import Cariage


class Locomotive(Cariage):
    def __init__(self, routes, seats, Locomotive_type, speed, weight):
        super().__init__(routes, seats, weight)