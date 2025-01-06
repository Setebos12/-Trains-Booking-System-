import networkx as nx
from matplotlib import pyplot as plt
from datetime import datetime
from Routes.Routes import Routes, create_graph_from_routes
from Routes.Route import Route


def draw_graph(routes):
    G = routes.routes

    plt.figure(figsize=(10, 6))
    nx.draw_circular(G, with_labels=True, node_color="skyblue", font_weight="bold", node_size=2000)
    plt.title("Routes Visualization")
    plt.show()


