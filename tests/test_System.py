from System.system import System, add_train_to_system, get_common
from networkx import DiGraph
from file_handle.train_files import read_all_trains
import networkx as nx
from matplotlib import pyplot as plt
import pytest
from System.system import RouteError, InvalidStationError
from System.MonitorUser import MonitorUserSystem


def test_incorpoate_To_bigger_graph():
    trains = read_all_trains()
    graph = DiGraph()
    for train in trains:
        graph = add_train_to_system(graph, train)

    assert len(graph.nodes['Warszawa Centralna']['arrivals']) > 0
    assert len(graph.nodes['Warszawa Centralna']['departure']) > 0


def test_all_path():
    system = System()

    paths = system.check_no_direct_connections("Radom Główny", "Sopot")
    assert len(paths) == 0
    paths = system.check_no_direct_connections("Olsztyn Główny", "Warszawa Centralna")
    assert len(paths) != 0


def test_set_common_elements():
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 3]
    assert get_common(nums1, nums2) == {2, 3}


def test_monitor_user():
    mont_user = MonitorUserSystem("0")
    assert mont_user.check_if_all_not_none() is False

    mont_user.route_id = 1
    mont_user.carriage_id = 1
    mont_user.user_id = 1
    mont_user.seat_id = 1
    mont_user.train_id = 1
    mont_user.deparute = 1
    mont_user.arrival = 1


def test_route_error():
    system = System()
    with pytest.raises(InvalidStationError):
        system.check_no_direct_connections("Nonexistent Station", "Another Nonexistent Station")


def test_monitor_user_invalid():
    mont_user = MonitorUserSystem("0")
    mont_user.route_id = None
    mont_user.carriage_id = None
    mont_user.user_id = None
    mont_user.seat_id = None
    mont_user.train_id = None
    mont_user.deparute = None
    mont_user.arrival = None

    assert mont_user.check_if_all_not_none() is False


def test_get_common_empty():
    nums1 = []
    nums2 = [2, 3]
    assert get_common(nums1, nums2) == set()

    nums1 = [1, 2, 3, 4]
    nums2 = []
    assert get_common(nums1, nums2) == set()


def test_get_common_no_common_elements():
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 7, 8]
    assert get_common(nums1, nums2) == set()

