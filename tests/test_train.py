from train.Seats import Seat


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