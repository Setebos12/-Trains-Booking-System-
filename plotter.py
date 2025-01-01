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


data1 = datetime(2024, 12, 29, 20, 30)
data2 = datetime(2024, 12, 29, 17, 30)
route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)

data1 = datetime(2024, 12, 29, 21, 30)
data2 = datetime(2024, 12, 29, 20, 45)
route2 = Route("Kraków", "Wrocław", data1, data2, 350)

data1 = datetime(2024, 12, 29, 22, 30)
data2 = datetime(2024, 12, 29, 22, 0)
route3 = Route("Wrocław", "Poznań", data1, data2, 180)

data1 = datetime(2024, 12, 30, 6, 0)
data2 = datetime(2024, 12, 30, 2, 30)
route4 = Route("Poznań", "Gdańsk", data1, data2, 410)

data1 = datetime(2024, 12, 30, 8, 30)
data2 = datetime(2024, 12, 30, 7, 0)
route5 = Route("Gdańsk", "Sopot", data1, data2, 10)


routes = Routes(1, create_graph_from_routes([route1, route2, route3, route4, route5]))

draw_graph(routes)

