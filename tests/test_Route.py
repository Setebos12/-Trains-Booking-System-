from Routes.Route import Route, NotDateTimeDatError
from Routes.Routes import Routes, CarriageRoutes
from datetime import datetime
import pytest


def test_create_Route():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route = Route("Warszawa Centralna", "Kraków", data1, data2, 300)

    assert route.starting_station == "Warszawa Centralna"
    assert route.destination_station == "Kraków"
    assert route.arrival_time() == data1
    assert route.departure_time() == data2
    assert route._distance == 300


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


def test_create_Routes():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data1 = datetime(2024, 12, 29, 21, 30)
    data2 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data1, data2, 350)
    routes = Routes(1, [route1, route2])

    assert list(routes.routes.nodes()) == ['Warszawa Centralna', 'Kraków', 'Wrocław']


def test_path_exist():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data1 = datetime(2024, 12, 29, 21, 30)
    data2 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data1, data2, 350)
    routes = Routes(1, [route1, route2])

    assert list(routes.routes.nodes()) == ['Warszawa Centralna', 'Kraków', 'Wrocław']
    assert routes.check_if_route_exist("Warszawa Centralna", "Wrocław") is True


def test_path_weight():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data1 = datetime(2024, 12, 29, 21, 30)
    data2 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data1, data2, 350)
    routes = Routes(1, [route1, route2])

    assert list(routes.routes.nodes()) == ['Warszawa Centralna', 'Kraków', 'Wrocław']
    assert routes.calculate_road("Warszawa Centralna", "Wrocław") == 650


def test_calculate_time():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data11 = datetime(2024, 12, 29, 21, 30)
    data22 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data11, data22, 350)
    routes = Routes(1, [route1, route2])

    assert routes.calculate_time('Warszawa Centralna', 'Wrocław') == data11 - data2


def test_CarriageRoutes():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data11 = datetime(2024, 12, 29, 21, 30)
    data22 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data11, data22, 350)
    seats_id = ['1', '2', '3', '4', '5']
    routes = Routes(1, [route1, route2])
    carriage_routes = CarriageRoutes(1, routes, seats_id)

    assert carriage_routes.seats_id == seats_id


def create_simple_CarriageRoutes():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data11 = datetime(2024, 12, 29, 21, 30)
    data22 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data11, data22, 350)
    seats_id = ['1', '2', '3', '4', '5']
    routes = Routes(1, [route1, route2])
    carriage_routes = CarriageRoutes(1, routes, seats_id)
    return carriage_routes, seats_id


def test_list_booked_seats():
    cr, seats_id = create_simple_CarriageRoutes()

    assert cr.list_booked_and_an_empy_seats("Warszawa Centralna", "Wrocław") == (set(seats_id), set())


def test_check_if_booked_is_possible():
    cr, seats_id = create_simple_CarriageRoutes()
    ans = cr.check_if_can_booked("Warszawa Centralna", "Wrocław", '1')
    assert ans is True
    cr.booked_seats("Warszawa Centralna", "Wrocław", '1', 123)
    ans = cr.check_if_can_booked("Warszawa Centralna", "Wrocław", '1')
    assert ans is False
    ans = cr.check_if_can_booked("Warszawa Centralna", "Kraków", '5')
    assert ans is True
    ans = cr.check_if_can_booked("Warszawa Centralna", "Kraków", '1')
    assert ans is False


def test_booked_seats():
    cr, seats_id = create_simple_CarriageRoutes()

    cr.booked_seats("Warszawa Centralna", "Wrocław", '1', 123)
    assert cr.routes.edges["Warszawa Centralna", "Kraków"]['seats']['1'] == 123
    assert cr.routes.edges["Kraków", "Wrocław"]['seats']['1'] == 123


def test_booked_seats_and_list_setas():
    cr, seats_id = create_simple_CarriageRoutes()

    cr.booked_seats("Warszawa Centralna", "Wrocław", '1', 123)

    ans = cr.list_booked_and_an_empy_seats("Warszawa Centralna", "Wrocław")
    assert ans == ({'2', '3', '4', '5'}, {'1'})
    ans = cr.list_booked_and_an_empy_seats("Warszawa Centralna", "Kraków")
    assert ans == ({'2', '3', '4', '5'}, {'1'})


def test_booked_seats_and_list_setas_one_station():
    cr, seats_id = create_simple_CarriageRoutes()

    cr.booked_seats("Warszawa Centralna", "Kraków", '1', 123)

    ans = cr.list_booked_and_an_empy_seats("Warszawa Centralna", "Wrocław")
    assert ans == ({'2', '3', '4', '5'}, {'1'})
    ans = cr.list_booked_and_an_empy_seats("Warszawa Centralna", "Kraków")
    assert ans == ({'2', '3', '4', '5'}, {'1'})
