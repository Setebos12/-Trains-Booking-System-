import json
from train.carriage import Cariage
from datetime import datetime
from train.Seats import Seat
from networkx.readwrite.json_graph import node_link_graph
from Routes.Routes import CarriageRoutes

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


def write_to_file_carriage(carriage: Cariage):
    data = carriage.carriage_repr()
    s1 = json.dumps(data, default=serialize_datetime, indent=4)
    uniq_id = str(carriage.id)
    file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Carriages/" + f"{uniq_id}.json" # relative path add
    with open(file_path, 'w') as file_handle:
        file_handle.write(s1)


def read_carriage(uniq_id):
    file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Carriages/" + f"{uniq_id}.json" # relative path add
    with open(file_path, 'r') as file_handle:
        file_data = file_handle.read()

    data = json.loads(file_data, object_hook=deserialize_datetime)
    return create_carriage_from_data(data)


def create_carriage_from_data(data):
    seats = [Seat(seat_data['id'],
                  seat_data['compartments'],
                  seat_data['window_middle_corridor'],
                  seat_data['table'],
                  seat_data['bike'],
                  seat_data['pregnat'],
                  seat_data['invalid']) for seat_data in data['seats']]
    seats_id = [seat_data['id'] for seat_data in data['seats']]
    graphs = {data['graph'][key]['id']:
              CarriageRoutes(data['graph'][key]['id'],
                             node_link_graph(data['graph'][key]['graph'], edges='links'),
                             seats_id, False) for key in data['graph']}

    carriage = Cariage(data['id'], graphs, seats, data['carriage_look'], False)
    return carriage