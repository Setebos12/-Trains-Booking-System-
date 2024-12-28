from train.carriage import Cariage
from train.Seats import Seat
from networkx.readwrite.json_graph import node_link_graph
from Routes.Routes import CarriageRoutes
from file_handle import read_data, write_data


def write_to_file_carriage(carriage: Cariage):
    # data = carriage.carriage_repr()
    # s1 = json.dumps(data, default=serialize_datetime, indent=4)
    # uniq_id = str(carriage.id)
    # file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Carriages/" + f"{uniq_id}.json" # relative path add
    # with open(file_path, 'w') as file_handle:
    #     file_handle.write(s1)
    write_data(carriage, base_path="data/Carriages")


def read_carriage(uniq_id):
    # file_path = "/home/krzysztof-rutkowski/pipr1/project1/data/Carriages/" + f"{uniq_id}.json" # relative path add
    # with open(file_path, 'r') as file_handle:
    #     file_data = file_handle.read()

    # data = json.loads(file_data, object_hook=deserialize_datetime)
    data = read_data(uniq_id, base_path="data/Carriages")
    return create_carriage_from_data(data)


def create_carriage_from_data(data):
    seats = [Seat(seat_data['id'],
                  seat_data['compartments'],
                  seat_data['window_middle_corridor'],
                  seat_data['table'],
                  seat_data['bike'],
                  seat_data['pregnat'],
                  seat_data['invalid']) for seat_data in data['seats']]
    seats_id = [seat_data.data['id'] for seat_data in seats]
    graphs = {data['graph'][key]['id']:
              CarriageRoutes(data['graph'][key]['id'],
                             node_link_graph(data['graph'][key]['graph'],
                                             edges='edges'),
                             seats_id, False) for key in data['graph']}

    carriage = Cariage(data['id'], graphs, seats, data['carriage_look'], False)
    return carriage
