from networkx.readwrite.json_graph import node_link_graph
from Routes.Routes import Routes
from train.train import Train
from train.carriage_files import create_carriage_from_data
from file_handle import write_data, read_data
from pathlib import Path


def write_train_file(train: Train):
    # data = train.json_repr()
    # s1 = json.dumps(data, default=serialize_datetime, indent=4)
    # uniq_id = str(train.id)
    # file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Trains/" + f"{uniq_id}.json" # relative path add
    # with open(file_path, 'w') as file_handle:
    #     file_handle.write(s1)
    write_data(train, base_path="data/Trains")


def read_train_file(uniq_id):
    # file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Trains/" + f"{uniq_id}.json" # relative path add
    # with open(file_path, 'r') as file_handle:
    #     file_data = file_handle.read()

    data = read_data(uniq_id, base_path="data/Trains")
    train_id = data['id']
    carriages = data['carrages']
    car = [create_carriage_from_data(carriage) for carriage in carriages.values()]
    routes = [Routes(route['id'],
                     node_link_graph(route['graph'], edges="edges"),
                     False) for route in data['routes'].values()]
    return Train(train_id, car, routes, False)


def read_all_trains():
    file_path = Path("data/Trains")
    all_trains = file_path.glob("*.json")

    trains = []
    for train in all_trains:
        id = train.stem
        trains.append(read_train_file(id))
    return trains
