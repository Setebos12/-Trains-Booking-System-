from train.train import Train
from Routes.Routes_files import read_Route
from train.carriage_files import read_carriage
from train.train_files import write_train_file, read_train_file
from train.train_files import read_all_trains
from pathlib import Path
from random import choice, sample, randint


def create_train(id, carriages_ids, route_ids):

    routes = [read_Route(route) for route in route_ids]
    carriages = [read_carriage(carriage) for carriage in carriages_ids]
    train = Train(id, carriages, routes)
    return train


def create_Random_trains():
    route_ids = get_ids("data/Routes_files")
    Carriage_id = get_ids("data/Carriages")
    index = 0
    while len(route_ids):
        route_id = choice(route_ids)
        route_ids.remove(route_id)
        carriages = sample(Carriage_id, randint(1, len(Carriage_id)))
        train1 = create_train(index, carriages, [route_id])
        write_train_file(train1)
        index += 1


def get_ids(path):
    base_path = Path(path)
    paths = list(base_path.glob("*.json"))
    ids = [path.stem for path in paths]
    return ids


create_Random_trains()
