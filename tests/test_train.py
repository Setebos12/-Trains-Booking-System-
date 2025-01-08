from train.Seats import Seat
from train.carriage import Cariage, assign_seats, create_carriage_routes
from Routes.Routes import Routes, SeatsinRouteBookedError, create_graph_from_routes
from Routes.Route import Route
import pytest
from train.train import Train, InvalidCarriageError
from file_handle.train_files import read_train_file
from datetime import datetime


def test_create_seat():
    seat = Seat(1, True, 2)

    assert seat.data['id'] == '1'
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
    r_data = {'compartments': True, 'id': '1'}
    assert seat.check_requirments(r_data) is True
    r_data = {'compartments': True, 'id': '35'}
    assert seat.check_requirments(r_data) is False
    r_data = {'compartments': True, 'id': '1', 'window_middle_corridor': 2}
    assert seat.check_requirments(r_data) is True


def create_simple_CarriageRoutes2():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route1 = Route("Warszawa Centralna", "Kraków", data1, data2, 300)
    data11 = datetime(2024, 12, 29, 21, 30)
    data22 = datetime(2024, 12, 29, 20, 45)
    route2 = Route("Kraków", "Wrocław", data11, data22, 350)
    carriage_routes = Routes(1, create_graph_from_routes([route1, route2]))
    return [carriage_routes]


def create_simple_CarriageRoutes22(seats):
    carriage_routes = create_simple_CarriageRoutes2()
    seats_id = [seat.data['id'] for seat in seats]
    return create_carriage_routes(carriage_routes, seats_id)


def test_create_carriage():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes22(seats)
    carriage = Cariage(1, carriage_routes, seats)

    assert carriage.id == 1
    assert len(carriage.seats) == len(seats)


def test_list_avalible_seats():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes22(seats)
    carriage = Cariage(1, carriage_routes, seats)

    ans = carriage.list_all_available_seats('Warszawa Centralna', 'Wrocław', 1)
    assert ans == ({'1', '2', '3'}, set())
    assert len(carriage.seats) == len(seats)


def test_list_avalible_seat_wrong_id_route():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes22(seats)
    carriage = Cariage(1, carriage_routes, seats)
    with pytest.raises(ValueError):
        carriage.list_all_available_seats('Warszawa Centralna', 'Wrocław', 2)


def test_list_avalible_test_book_seat():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes22(seats)
    carriage = Cariage(1, carriage_routes, seats)

    carriage.book_seat_for_route('Warszawa Centralna', 'Wrocław', str(2), 1, 123)
    ans = carriage.list_all_available_seats('Warszawa Centralna', 'Wrocław', 1)
    assert ans == ({'1', '3'}, {'2'})


def test_filter_seats():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, False, 0)}

    carriage_routes = create_simple_CarriageRoutes22(seats)
    carriage = Cariage(1, carriage_routes, seats)

    carriage.book_seat_for_route('Warszawa Centralna', 'Wrocław', '2', 1, 123)
    ans = carriage.filter_seats({"window_middle_corridor": 0})
    assert ans == {'3'}
    ans = carriage.filter_seats({"compartments": True})
    assert ans == {'1', '2'}


def test_get_carriage_look():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes22(seats)
    carriage = Cariage(1, carriage_routes, seats, [['.', 'S1', 'S2', 'S3']])

    carriage.book_seat_for_route('Warszawa Centralna', 'Wrocław', '2', 1, 123)
    seats = carriage.list_all_available_seats('Warszawa Centralna', 'Wrocław', 1)
    ans = carriage.get_carriage_look(seats)
    assert ans == [['.', 'S1F', 'S2B', 'S3F']]


def test_create_train():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats, [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)

    assert train.carriages[1] == carriage1
    assert train.carriages[2] == carriage2
    assert train.carriages[3] == carriage3


def test_book_seat_train():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats.copy(), [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats.copy(), [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats.copy(), [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)
    train.assign_routes_to_carriages()
    assert type(train.routes[1]) is Routes
    train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=1, seat_id='1', route_id=1, data=123)
    train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=2, seat_id='1', route_id=1, data=123)

    assert train.carriages[1].list_all_available_seats("Warszawa Centralna", "Kraków", 1) == ({'2', '3'}, {'1'})
    with pytest.raises(SeatsinRouteBookedError):
        train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=1, seat_id='1', route_id=1, data=123)


def test_book_seat_train_wrong_id_carriage_seat_route():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats, [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)
    train.assign_routes_to_carriages()

    with pytest.raises(InvalidCarriageError):
        train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=5, seat_id='1', route_id=1, data=123)
    with pytest.raises(KeyError):
        train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=2, seat_id='4', route_id=1, data=123)
    with pytest.raises(ValueError):
        train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=2, seat_id='2', route_id=6, data=123)


def test_all_avalble_seats():
    seats = {Seat(1, True, 2),
             Seat(2, True, 1),
             Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats, [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)
    train.assign_routes_to_carriages()

    ans = train.list_all_available_seats('Warszawa Centralna', 'Wrocław', 1)
    assert ans == {1: ({'1', '2', '3'}, set()), 2: ({'1', '2', '3'}, set()), 3: ({'1', '2', '3'}, set())}

    train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=1, seat_id=1, route_id=1, data=123)
    train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=2, seat_id=1, route_id=1, data=123)
    train.book_seat_for_route('Warszawa Centralna', 'Wrocław', carriage_id=3, seat_id=2, route_id=1, data=123)

    ans = train.list_all_available_seats('Warszawa Centralna', 'Wrocław', 1)

    assert ans == {1: ({'2', '3'}, {'1'}), 2: ({'2', '3'}, {'1'}), 3: ({'1', '3'}, {'2'})}


def test_remove_carriage():
    seats = {Seat(1, True, 2),
                Seat(2, True, 1),
                Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats, [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)
    train.remove_carriage(2)

    assert 2 not in train.carriages
    assert len(train.carriages) == 2


def test_add_carriage():
    seats = {Seat(1, True, 2),
                Seat(2, True, 1),
                Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage4 = Cariage(4, {}, seats, [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)
    train.add_carriage(carriage4)

    assert train.carriages[4] == carriage4
    assert len(train.carriages) == 4


def test_add_existing_carriage():
    seats = {Seat(1, True, 2),
                Seat(2, True, 1),
                Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats, [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)

    with pytest.raises(InvalidCarriageError):
        train.add_carriage(carriage2)


def test_remove_nonexistent_carriage():
    seats = {Seat(1, True, 2),
                Seat(2, True, 1),
                Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats, [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)

    with pytest.raises(InvalidCarriageError):
        train.remove_carriage(4)


def test_list_of_ids():
    seats = {Seat(1, True, 2),
                Seat(2, True, 1),
                Seat(3, True, 0)}

    carriage_routes = create_simple_CarriageRoutes2()
    carriage1 = Cariage(1, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage2 = Cariage(2, {}, seats, [['.', 'S1', 'S2', 'S3']])
    carriage3 = Cariage(3, {}, seats, [['.', 'S1', 'S2', 'S3']])

    train = Train(1, [carriage1, carriage2, carriage3], carriage_routes)

    assert train.list_of_ids() == [1]
