from get_data.get_data import get_all_stations_info
from Routes.Route import Route
from Routes.Routes import Routes, create_graph_from_routes
from datetime import datetime
from file_handle.Routes_files import write_Route
from file_handle.file_handle import read_list


data = read_list('data/Routes_internet_data.txt')


def convert_to_datetime(time_string, current_date: datetime):
    converted_datetime = datetime.strptime(time_string, "%H:%M").replace(
        year=current_date.year,
        month=current_date.month,
        day=current_date.day
    )

    return converted_datetime


def get_one_train_Route(routes, id, current_date: datetime):
    routes_statios = []
    last_distance = 0
    for index in range(len(routes)-1):
        starting_station = routes[index]
        destination_station = routes[index+1]

        arrival_time = convert_to_datetime(destination_station['arrival_time'], current_date)
        departure_time = convert_to_datetime(starting_station['departure_time'], current_date)
        route_station = Route(starting_station['station'],
                              destination_station['station'],
                              arrival_time,
                              departure_time,
                              float(starting_station['distance'])-last_distance)
        routes_statios.append(route_station)
        last_distance = float(starting_station['distance'])
    routes = Routes(id, create_graph_from_routes(routes_statios))
    return routes


def write_routes(data, current_date: datetime, indexFrom: int = 0):
    trains = []
    for index, url in enumerate(data):
        train = get_all_stations_info(url)
        trains.append(get_one_train_Route(train, index+indexFrom, current_date))
        write_Route(trains[index])
