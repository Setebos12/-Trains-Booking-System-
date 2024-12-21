from Routes.Route import Route
from networkx import DiGraph


class Routes:
    """Routes will be in nx graph
    each node of graph is station : data in node (departure_time, arrival_time)
    each edge is road : data is (distance, data_booked)
    """
    def __init__(self, routes: list[Route]):
        self.routes = DiGraph()
        self.current_station = routes[0].starting_station()
        for route in routes:
            self.routes.add_node(route.starting_station(), departure_time=route.departure_time())

        for route in routes:
            self.routes.add_edge(route.starting_station(), route.destination_station(), data=route)
            self.routes.nodes[route.destination_station()]["arrival_time"] = route.arrival_time()


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
