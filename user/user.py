import json


class User:
    def __init__(self, id, name: str, surname: str, password: str, login: str, tickets=None):
        self.id = id
        self.name = name
        self.surname = surname
        self._password = password
        self.login = login
        self.tickets = tickets if tickets is not None else []

    def __str__(self):
        return f"{self.name}  {self.surname}"

    def json_repr(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'password': self._password,
            'login': self.login,
            'tickets': [ticket.json_repre() for ticket in self.tickets]
        }


def write_user_file(user: User):
    data = user.json_repr()
    s1 = json.dumps(data, indent=4)
    uniq_id = user.id
    file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Users/" + f"{uniq_id}.json" # relative path add
    with open(file_path, 'w') as file_handle:
        file_handle.write(s1)


def read_user(id: str):
    file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Users/" + f"{id}.json" # relative path add
    with open(file_path, 'r') as file_handle:
        data = json.load(file_handle)

    return User(data['id'], data['name'], data['surname'], data['password'], data['login'], data['tickets'])

