from System.system import System, add_train_to_system
from networkx import DiGraph
from train.train_files import read_all_trains
import networkx as nx
from matplotlib import pyplot as plt


def test_incorpoate_To_bigger_graph():
    trains = read_all_trains()
    graph = DiGraph()
    for train in trains:
        graph = add_train_to_system(graph, train)

    assert len(graph.nodes['Warszawa Centralna']['arrivals']) > 0
    assert len(graph.nodes['Warszawa Centralna']['departure']) > 0
