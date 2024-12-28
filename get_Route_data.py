from get_data import get_all_stations_info
from Routes.Route import Route
from Routes.Routes import Routes, create_graph_from_routes
from datetime import datetime
from Routes.Routes_files import write_Route
from file_handle import read_list


data = read_list('data/Routes_internet_data.txt')


def convert_to_datetime(time_string):
    current_date = datetime(2025, 1, 16)

    converted_datetime = datetime.strptime(time_string, "%H:%M").replace(
        year=current_date.year,
        month=current_date.month,
        day=current_date.day
    )

    return converted_datetime


def get_one_train_Route(routes, id):
    routes_statios = []
    last_distance = 0
    for index in range(len(routes)-1):
        starting_station = routes[index]
        destination_station = routes[index+1]

        arrival_time = convert_to_datetime(destination_station['arrival_time'])
        departure_time = convert_to_datetime(starting_station['departure_time'])
        route_station = Route(starting_station['station'],
                            destination_station['station'],
                            arrival_time,
                            departure_time,
                            float(starting_station['distance'])-last_distance)
        routes_statios.append(route_station)
        last_distance = float(starting_station['distance'])
    routes = Routes(id, create_graph_from_routes(routes_statios))
    return routes


def write_routes(data):
    trains = []
    for index, url in enumerate(data):
        train = get_all_stations_info(url)
        trains.append(get_one_train_Route(train, index))
        write_Route(trains[index])

write_routes(data)



# look = [['.', 'S', 'S'],
#  ['.', 'S', 'S'],
#  ['.', 'S', 'S'],
#  ['.', 'S', 'S'],
#  ['.', 'S', 'S'],
#  ['.', 'S', 'S'],]

# seats = [Seat(1, True, 2), Seat(2, True, 0),
#         Seat(3, True, 2), Seat(4, True, 0),
#         Seat(5, True, 2), Seat(6, True, 0),
#         Seat(7, True, 2), Seat(8, True, 0),
#         Seat(9, True, 2), Seat(10, True, 0),
#         Seat(11, True, 2), Seat(12, True, 0)]

# carriage = Cariage(0, [], seats, look)
# print(carriage.json_repr())

# write_to_file_carriage(carriage)

# look2 = [['.', 'S1', 'S2'],
#  ['.', 'T', 'T'],
#  ['.', 'S3', 'S4'],
#  ['.', 'S5', 'S6'],
#  ['.', 'T', 'T'],
#  ['.', 'S7', 'S8'],]

# seats1 = [
#     Seat(1, True, 2, table=True), Seat(2, True, 0, table=True),
#     Seat(3, True, 2, table=True), Seat(4, True, 0, table=True),
#     Seat(5, True, 2, table=True), Seat(6, True, 0, table=True),
#     Seat(7, True, 2, table=True), Seat(8, True, 0, table=True)
# ]


# routes  = read_Route(1)

# carriage1 = Cariage(1, [], seats1, look2)
# write_to_file_carriage(carriage1)

# carriage = read_carriage(1)

# print(carriage.json_repr()['graph'])