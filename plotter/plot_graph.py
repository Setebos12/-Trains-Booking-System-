import networkx as nx
from matplotlib import pyplot as plt
from get_data.get_data import get_station_data
from System.system import System


def draw_graph(routes):
    G = routes
    stations = routes.nodes
    station_positions = get_stations_gps(stations)

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos=station_positions, with_labels=True, node_color="skyblue", font_weight="bold", node_size=200, font_size=6)
    plt.show()


def get_stations_gps(stations):
    station_positions = {}

    for station in stations:
        name, address, gps = get_station_data("https://portalpasazera.pl/KatalogStacji/Index?stacja=" + str(station))
        station_positions[station] = (float(gps[1].replace(',', '.')), float(gps[0].replace(',', '.')))
    return station_positions

