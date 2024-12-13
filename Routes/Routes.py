from Routes.Route import Route


class Routes:
    """Routes will be in nx graph 
    each node of graph is station : data in node (starting_station, destination_station, departure_time, arrival_time)
    each edge is road : data is (distance, data_booked)
    """
    def __init__(self, routes: list[Route], arrival_time, departure_time):
        pass

    def check_if_route_exist(self, starting_station: str, destination_station: str) -> bool:
        pass

    def calculate_road(self, starting_station: str, destination_station: str) -> int:
        pass

    def book_route(self, starting_station: str, destination_station: str, data):
        pass

    def undo_book_route(self, starting_station: str, destination_station: str):
        pass

    def calculate_time(self, starting_station: str, destination_station: str):
        pass
