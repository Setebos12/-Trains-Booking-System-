from train.train import Train
from networkx import DiGraph, compose, has_path, all_simple_paths
from train.train_files import read_all_trains


class System:
    def __init__(self, trains: list[Train]):
        self.trains = {train.id: train for train in trains}

    def create_graph_from_trains(self):
        trains = read_all_trains()
        graph = DiGraph()
        for train in trains:
            graph = add_train_to_system(graph, train)
        self.network = graph

    def check_direct_connection(self, starting_station, destination_station):
        if has_path(self.network, starting_station, destination_station) is False:
            raise ValueError # create some error no path error

        start_deparutes = self.network.nodes[starting_station]['departure'].copy()
        destin_arrival = self.network.nodes[destination_station]['arrivals'].copy()
        common_keys = list(get_common(start_deparutes, destin_arrival))
        return common_keys

    def check_all_connections(self, starting_station, destination_station):
        if has_path(self.network, starting_station, destination_station) is False:
            raise ValueError # create some error no path error

        paths = all_simple_paths(starting_station, destination_station)
        pass



def get_common(nums1, nums2):
    return set(nums1) & set(nums2)



def merge_Graphs(G: DiGraph, grap_routes: DiGraph, train_id, route_id):

    graph = grap_routes.copy()
    data_nodes = dict(grap_routes.nodes(data=True))
    for node in graph.nodes:
        graph.nodes[node].clear()

    merger_graph = compose(G, graph)
    for node in data_nodes:
        if 'arrivals' not in merger_graph.nodes[node]:
            merger_graph.nodes[node]['arrivals'] = {}
        if 'departure' not in merger_graph.nodes[node]:
            merger_graph.nodes[node]['departure'] = {}

        if 'arrival_time' in data_nodes[node]:
            merger_graph.nodes[node]['arrivals'][(route_id, train_id)] = data_nodes[node]['arrival_time']
        if 'departure_time' in data_nodes[node]:
            merger_graph.nodes[node]['departure'][(route_id, train_id)] = data_nodes[node]['departure_time']
    return merger_graph


def add_train_to_system(G: DiGraph, train: Train):
    train_id = train.id
    for route in train.routes:
        G = merge_Graphs(G, train.routes[route].routes, train_id, route)
    return G
