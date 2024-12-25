from System.system import System, add_train_to_system, get_common
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


def test_set_common_elements():
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 3]
    assert get_common(nums1, nums2) == {2, 3}