from train.train import Train
from Routes.Routes_files import read_Route
from train.carriage_files import read_carriage
from train.train_files import write_train_file, read_train_file, read_all_trains
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
# train = create_train(1, [0, 1], [0])
# train1 = create_train(2, [0], [1])
# train2 = create_train(3, [1], [2])
# train3 = create_train(4, [1, 0], [3])


# write_train_file(train)
# write_train_file(train1)
# write_train_file(train2)
# write_train_file(train3)
# train = read_train_file(1)
# write_train_file(train)


# trains = read_all_trains()
# pass