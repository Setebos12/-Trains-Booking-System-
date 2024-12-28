from System.system import System, add_train_to_system, get_common
from networkx import DiGraph
from train.train_files import read_all_trains
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
    trains = read_all_trains()
    system = System(trains)
    system.create_graph_from_trains() # change to go outside class

    assert set(system.check_direct_connection("Radom Główny", "Sopot")) == set()
    assert set(system.check_direct_connection("Olsztyn Główny", "Sopot")) == set()
    assert set(system.check_direct_connection("Olsztyn Główny", "Kraków Główny")) == {(3, 4)}
    assert set(system.check_direct_connection("Warszawa Centralna", "Warszawa Zachodnia")) == {(3, 4)}


def test_direct_path_no_path():
    trains = read_all_trains()
    system = System(trains)
    system.create_graph_from_trains() # change to go outside class

    with pytest.raises(RouteError):
        system.check_direct_connection("Sopot", "Warszawa Centralna")


def test_all_path():
    trains = read_all_trains()
    system = System(trains)
    system.create_graph_from_trains()

    paths = system.check_no_direct_connections("Radom Główny", "Sopot")
    assert paths == []
    paths = system.check_no_direct_connections("Olsztyn Główny", "Warszawa Centralna")
    assert len(paths) == 0


def test_check_transfer():
    trains = read_all_trains()
    system = System(trains)
    system.create_graph_from_trains()

    assert system.check_stations_correct_transfers((3, 4), (0, 1), "Warszawa Centralna") == (0, 0)
    assert system.check_stations_correct_transfers((3, 4), (2, 3), "Warszawa Centralna") == (0, 0)


def test_list_all_avalible_seats():
    trains = read_all_trains()
    system = System(trains)
    system.create_graph_from_trains()

    data = system.list_all_availabe_seats("Olsztyn Główny", "Kraków Główny", 3, 4, {'table': True})
    assert len(data) > 0

def test_set_common_elements():
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 3]
    assert get_common(nums1, nums2) == {2, 3}