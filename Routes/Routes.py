from Routes.Route import Route
from networkx import DiGraph, has_path, shortest_path, shortest_path_length


class Routes:
    """Routes will be in nx graph
    each node of graph is station : data in node (departure_time, arrival_time)
    each edge is road : data is (distance, data_booked)
    """
    def __init__(self, routes: list[Route]):
        self.routes = DiGraph()
        self.current_station = routes[0].starting_station
        for route in routes:
            self.routes.add_node(route.starting_station, departure_time=route.departure_time())

        for route in routes:
            self.routes.add_edge(route.starting_station,
                                 route.destination_station,
                                 weight=route.distance(),
                                 )
            self.routes.nodes[route.destination_station]["arrival_time"] = route.arrival_time()

    def check_if_route_exist(self, starting_station: str, destination_station: str) -> bool:
        return has_path(self.routes, starting_station, destination_station)

    def calculate_road(self, starting_station: str, destination_station: str) -> int:
        return shortest_path_length(
            self.routes,
            starting_station,
            destination_station,
            weight='weight'
        )

    def stations_between(self, starting_station: str, destination_station: str):
        return shortest_path(self.routes, starting_station, destination_station)

    def calculate_time(self, starting_station: str, destination_station: str):
        departtime = self.routes.nodes[starting_station]['departure_time']
        arrivetime = self.routes.nodes[destination_station]['arrival_time']
        return arrivetime-departtime


class CarriageRoutes(Routes):
    def __init__(self, routes, seats_id):
        super().__init__(routes)
        seats_booked = {seat_id: None for seat_id in seats_id}
        self.routes.edges['seats'] = seats_booked


def make_tuple_from_list(self, nums):
    return [(nums[index], nums[index+1]) for index in range(len(nums)-1)]
