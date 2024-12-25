import json
from train.carriage import Cariage
from datetime import datetime
from train.Seats import Seat
from networkx.readwrite.json_graph import node_link_graph
from Routes.Routes import Routes
from train.train import Train
from train.carriage_files import create_carriage_from_data
from pathlib import Path, PosixPath



def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def deserialize_datetime(obj):
    for key, value in obj.items():
        if isinstance(value, str):
            try:
                obj[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return obj


def write_train_file(train: Train):
    data = train.json_repr()
    s1 = json.dumps(data, default=serialize_datetime, indent=4)
    uniq_id = str(train.id)
    file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Trains/" + f"{uniq_id}.json" # relative path add
    with open(file_path, 'w') as file_handle:
        file_handle.write(s1)


def read_train_file(uniq_id):
    file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Trains/" + f"{uniq_id}.json" # relative path add
    with open(file_path, 'r') as file_handle:
        file_data = file_handle.read()

    data = json.loads(file_data, object_hook=deserialize_datetime)
    train_id = data['id']
    carriages = data['carrages']
    car = [create_carriage_from_data(carriage) for carriage in carriages.values()]
    routes = [Routes(route['id'],
                     node_link_graph(route['graph'], edges="links"),
                     False) for route in data['routes'].values()]
    return Train(train_id, car, routes)


def read_all_trains():
    file_path = Path("/home/krzysztof-rutkowski/pipr1/project1/data/Trains/")
    all_trains = file_path.glob("*.json")

    trains = []
    for train in all_trains:
        id = train.stem
        trains.append(read_train_file(id))
    return trains



