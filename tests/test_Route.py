from Routes.Route import Route, NotDateTimeDatError
from Routes.Routes import Routes
from datetime import datetime
import pytest


def test_create_Route():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route = Route("Warszawa Centralna", "Kraków", data1, data2, 300)

    assert route.starting_station() == "Warszawa Centralna"
    assert route.destination_station() == "Kraków"
    assert route.arrival_time() == data1
    assert route.departure_time() == data2
    assert route._distance == 300
    assert route.is_booked() is False


def test_create_Route_no_datatime():
    data1 = (2024, 12, 29, 20, 30)
    data2 = (2024, 12, 29, 17, 30)
    with pytest.raises(NotDateTimeDatError):
        Route("Warszawa Centralna", "Kraków", data1, data2, 300)


def test_create_Route_negative_time():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    with pytest.raises(ValueError):
        Route("Warszawa Centralna", "Kraków", data2, data1, 300)


def test_create_Route_negative_distance():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    with pytest.raises(ValueError):
        Route("Warszawa Centralna", "Kraków", data2, data1, -1)


def test_book_route_and_undo_root():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route = Route("Warszawa Centralna", "Kraków", data1, data2, 300)

    assert route.is_booked() is False
    data = 123
    route.book_route(data)
    assert route.booked_data == 123
    assert route.is_booked() is True
    route.undo_book_route()
    assert route.is_booked() is False


def test_create_Routes():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data1 = datetime(2024, 12, 29, 21, 30)
    data2 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data1, data2, 350)
    routes = Routes([route1, route2])

    assert list(routes.routes.nodes()) == ['Warszawa Centralna', 'Kraków', 'Wrocław']


def test_path_exist():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data1 = datetime(2024, 12, 29, 21, 30)
    data2 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data1, data2, 350)
    routes = Routes([route1, route2])

    assert list(routes.routes.nodes()) == ['Warszawa Centralna', 'Kraków', 'Wrocław']
    assert routes.check_if_route_exist("Warszawa Centralna", "Wrocław") is True


def test_path_weight():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data1 = datetime(2024, 12, 29, 21, 30)
    data2 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data1, data2, 350)
    routes = Routes([route1, route2])

    assert list(routes.routes.nodes()) == ['Warszawa Centralna', 'Kraków', 'Wrocław']
    assert routes.calculate_road("Warszawa Centralna", "Wrocław") == 650