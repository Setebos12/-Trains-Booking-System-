from file_handle.file_handle import read_list, remove_folder
from get_data.get_Route_data import write_routes
from get_data.create_trains import create_Random_trains
from train.Seats import Seat
from train.carriage import Cariage, json_repr_carriage, assign_seats
from file_handle.carriage_files import write_to_file_carriage
from get_data.create_carriages import create_carriages
from datetime import datetime, timedelta

if __name__ == "__main__":
    data = read_list('data/Routes_internet_data.txt') # reads urls with data

    valid_paths = {"data/Users", "data/Trains", "data/Routes_files", "data/Carriages"}

    for path in valid_paths:
        remove_folder(path)
    create_carriages()
    for index in range(1):
        date = datetime.now() + timedelta(days=index+20)
        write_routes(data, date, indexFrom=len(data)*index)
    create_Random_trains()