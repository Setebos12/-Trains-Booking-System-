from Routes.Route import Route
from networkx import Graph


class Routes:
    """Routes will be in nx graph
    each node of graph is station : data in node (starting_station, destination_station, departure_time, arrival_time)
    each edge is road : data is (distance, data_booked)
    """
    def __init__(self, routes: list[Route]):
        self.routes = Graph()
        for route in routes:
            self.routes.add_node(route.starting_station())
        for route in routes:
            self.routes.add_edge(route.starting_station(), route.destination_station(), data=route)
            self.routes.degree(route.disctance())

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
