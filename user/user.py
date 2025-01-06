import json
from user.ticket import Ticket, json_repr_ticket
from pathlib import Path


class User:
    def __init__(self, id, tickets: list[Ticket] = None):
        self.id = id
        self.tickets = []
        if tickets:
            self.tickets = tickets

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)

    def remove_ticket(self, ticket: Ticket):
        if ticket in self.tickets:
            self.tickets.remove(ticket)

    def __str__(self):
        return f"{self.id}"


def json_repr_user(user: User):
    return {
        'id': user.id,
        'tickets': [json_repr_ticket(ticket) for ticket in user.tickets]
    }


def write_user_file(user: User, base_path="data/Users"):
    base_path = Path(base_path)
    base_path.mkdir(parents=True, exist_ok=True)

    file_path = base_path / f"{user.id}.json"
    data = json_repr_user(user)
    with file_path.open('w') as file_handle:
        json.dump(data, file_handle, indent=4)


def read_user(id: str, base_path="data/Users"):
    base_path = Path(base_path)
    file_path = base_path / f"{id}.json"

    if not file_path.exists():
        raise FileNotFoundError(f"User file {file_path} not found.")

    with file_path.open('r') as file_handle:
        data = json.load(file_handle)

    tickets = [
        Ticket(
            ticket_data['start_station'],
            ticket_data['end_station'],
            ticket_data['train_id'],
            ticket_data['route_id'],
            ticket_data['carriage_id'],
            ticket_data['seat_id'],
            arrival_time=ticket_data['arrival_time'],
            departure_time=ticket_data['departure_time']
        ) for ticket_data in data.get('tickets', [])
    ]

    return User(data['id'], tickets)


def get_all_users(base_path="data/Users"):
    base_path = Path(base_path)

    if not base_path.exists():
        raise FileNotFoundError(f"Directory {base_path} does not exist.")

    users = []
    for file_path in base_path.glob("*.json"):
        user_id = file_path.stem

        user = read_user(user_id, base_path=base_path)
        users.append(user)
    return users
