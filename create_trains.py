from train.train import Train
from Routes.Routes_files import read_Route
from train.carriage_files import read_carriage
from train.train_files import write_train_file, read_train_file


def create_train(id, carriages_ids, route_ids):

    routes = [read_Route(route) for route in route_ids]
    carriages = [read_carriage(carriage) for carriage in carriages_ids]
    train = Train(1, carriages, routes)
    return train


train = create_train(1, [0, 1], [0])
write_train_file(train)

train = read_train_file(1)
write_train_file(train)
pass