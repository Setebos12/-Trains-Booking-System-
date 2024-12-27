import json
from user.ticket import Ticket
import os


class User:
    def __init__(self, id, tickets: list[Ticket] = None):
        self.id = id
        self.tickets = []
        if tickets:
            self.tickets = tickets

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)

    def __str__(self):
        return f"{self.id}"

    def json_repr(self):
        return {
            'id': self.id,
            'tickets': [ticket.json_repr() for ticket in self.tickets]
        }


def write_user_file(user: User, base_path="data/Users"):
    data = user.json_repr()
    s1 = json.dumps(data, indent=4)
    uniq_id = user.id
    file_path = os.path.join(base_path, f"{uniq_id}.json")
    os.makedirs(base_path, exist_ok=True)  # Ensure directory exists
    with open(file_path, 'w') as file_handle:
        file_handle.write(s1)


def read_user(id: str, base_path="data/Users"):
    file_path = os.path.join(base_path, f"{id}.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"User file {file_path} not found.")

    with open(file_path, 'r') as file_handle:
        data = json.load(file_handle)

    tickets = [
        Ticket(
            ticket_data['start_station'],
            ticket_data['end_station'],
            ticket_data['train_id'],
            ticket_data['route_id'],
            ticket_data['carriage_id'],
            ticket_data['seat_id']
        ) for ticket_data in data.get('tickets', [])
    ]

    return User(data['id'], tickets)


def get_all_users(base_path="data/Users"):
    users = []

    if not os.path.exists(base_path):
        raise FileNotFoundError(f"Directory {base_path} does not exist.")
    for file_name in os.listdir(base_path):

        if file_name.endswith(".json"):
            user_id = os.path.splitext(file_name)[0]

            try:
                user = read_user(user_id, base_path=base_path)
                users.append(user)
            except Exception as e:
                print(f"Failed to read user from file {file_name}: {e}")

    return users
