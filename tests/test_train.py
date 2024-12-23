from train.Seats import Seat
from train.carriage import Cariage
from Routes.Routes import Routes
from Routes.Route import Route
import pytest
from datetime import datetime


def test_create_seat():
    seat = Seat(1, True, 2)

    assert seat.data['id'] == 1
    assert seat.data['compartments'] is True
    assert seat.data['window_middle_corridor'] == 2
    assert seat.data['table'] is False
    assert seat.data['bike'] is False
    assert seat.data['pregnat'] is False
    assert seat.data['invalid'] is False


def test_check_requriments():
    seat = Seat(1, True, 2)
    r_data = {}
    assert seat.check_requirments(r_data) is True


def test_check_requriments_compartmnets():
    seat = Seat(1, True, 2)
    r_data = {'compartments': False, 'id': 1}
    assert seat.check_requirments(r_data) is False


def test_check_requriments_id():
    seat = Seat(1, True, 2)
    r_data = {'compartments': True, 'id': 1}
    assert seat.check_requirments(r_data) is True
    r_data = {'compartments': True, 'id': 35}
    assert seat.check_requirments(r_data) is False
    r_data = {'compartments': True, 'id': 1, 'window_middle_corridor': 2}
    assert seat.check_requirments(r_data) is True


def create_simple_CarriageRoutes():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data11 = datetime(2024, 12, 29, 21, 30)
    data22 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data11, data22, 350)
    carriage_routes = Routes(1, [route1, route2])
    return carriage_routes


def test_create_carriage():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes()
    carriage = Cariage(1, [carriage_routes], seats)

    assert carriage.id == 1
    assert carriage.seats == seats


def test_create_carriage_list_avalible_seats():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes()
    carriage = Cariage(1, [carriage_routes], seats)
    ans = carriage.list_all_availabe_seats('Warszawa Centralna', 'Wrocław', 1)
    assert ans == ({1, 2, 3}, set())
    assert carriage.seats == seats


def test_create_carriage_list_avalible_seat_wrong_id_route():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes()
    carriage = Cariage(1, [carriage_routes], seats)
    with pytest.raises(ValueError):
        carriage.list_all_availabe_seats('Warszawa Centralna', 'Wrocław', 2)


def test_create_carriage_list_avalible_test_book_seat():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes()
    carriage = Cariage(1, [carriage_routes], seats)

    carriage.book_seat_for_route('Warszawa Centralna', 'Wrocław', 2, 1, 123)
    ans = carriage.list_all_availabe_seats('Warszawa Centralna', 'Wrocław', 1)
    assert ans == ({1, 3}, {2})