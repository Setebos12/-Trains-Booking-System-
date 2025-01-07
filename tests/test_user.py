from user.ticket import Ticket
from user.user import User, write_user_file, read_user, get_all_users
import pytest


def test_create_ticket():
    ticket = Ticket("Warsaw", "Vien", 1, 1, 1, 1, "10", "20")

    assert ticket.carriage_id == 1
    assert ticket.route_id == 1
    assert ticket.train_id == 1
    assert ticket.end_station == "Vien"
    assert ticket.start_station == 'Warsaw'


def test_create_user():
    user = User(1)
    assert user.id == 1


def test_write_read_user_file():
    user = User(1)
    ticket = Ticket("Warsaw", "Vien", 1, 1, 1, 1, "10", "20")
    user.add_ticket(ticket)

    write_user_file(user)
    user1 = read_user(1)

    assert user1.id == 1
    assert user1.tickets[0].carriage_id == 1
    assert user1.tickets[0].start_station == 'Warsaw'
    assert user1.tickets[0].end_station == 'Vien'


def test_add_ticket():
    user = User(1)
    ticket = Ticket("Warsaw", "Vien", 1, 1, 1, 1, "10", "20")
    user.add_ticket(ticket)

    assert len(user.tickets) == 1
    assert user.tickets[0] == ticket


def test_remove_ticket():
    user = User(1)
    ticket = Ticket("Warsaw", "Vien", 1, 1, 1, 1, "10", "20")
    user.add_ticket(ticket)
    user.remove_ticket(ticket)

    assert len(user.tickets) == 0


def test_remove_nonexistent_ticket():
    user = User(1)
    ticket1 = Ticket("Warsaw", "Vien", 1, 1, 1, 1, "10", "20")
    ticket2 = Ticket("Berlin", "Paris", 2, 2, 2, 2, "15", "25")
    user.add_ticket(ticket1)
    user.remove_ticket(ticket2)

    assert len(user.tickets) == 1
    assert user.tickets[0] == ticket1




