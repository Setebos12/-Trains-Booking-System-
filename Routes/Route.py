import networkx as nx


class Route:
    """Routes will be in nx graph 
    each node of graph is station : data in node (starting_station, destination_station, departure_time, arrival_time)
    each edge is road : data is (distance, data_booked)
    """
    def __init__(self, starting_station: str, destination_station: str, arrival_time, departure_time, distance):
        pass

    def book_route(self):
        pass

    def is_booked(self) -> bool:
        pass

    def undo_book_route(self):
        pass

    def set_arrive_time_departure_time(self, arrival_time, departure_time):
        pass


