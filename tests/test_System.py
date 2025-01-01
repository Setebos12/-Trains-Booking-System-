from System.system import System, add_train_to_system, get_common
from networkx import DiGraph
from file_handle.train_files import read_all_trains
import networkx as nx
from matplotlib import pyplot as plt
import pytest
from System.system import RouteError


def test_incorpoate_To_bigger_graph():
    trains = read_all_trains()
    graph = DiGraph()
    for train in trains:
        graph = add_train_to_system(graph, train)

    assert len(graph.nodes['Warszawa Centralna']['arrivals']) > 0
    assert len(graph.nodes['Warszawa Centralna']['departure']) > 0


def test_direct_path():
    system = System()


    assert set(system.check_direct_connection("Radom Główny", "Sopot")) == set()
    assert set(system.check_direct_connection("Olsztyn Główny", "Sopot")) == {(9, 12)}
    assert set(system.check_direct_connection("Olsztyn Główny", "Kraków Główny")) == {(3, 5)}
    assert len(set(system.check_direct_connection("Warszawa Centralna", "Warszawa Zachodnia"))) > 0


def test_all_path():
    system = System()
    system.create_graph_from_trains()

    paths = system.check_no_direct_connections("Radom Główny", "Sopot")
    assert len(paths) == 0
    paths = system.check_no_direct_connections("Olsztyn Główny", "Warszawa Centralna")
    assert len(paths) != 0


def test_set_common_elements():
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 3]
    assert get_common(nums1, nums2) == {2, 3}