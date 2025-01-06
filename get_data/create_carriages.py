from train.Seats import Seat
from train.carriage import Cariage
from file_handle.carriage_files import write_to_file_carriage


def create_carriages():
    look = [['.', 'S1', 'S2'],
            ['.', 'S3', 'S4'],
            ['.', 'S5', 'S6'],
            ['.', 'S7', 'S8'],
            ['.', 'S9', 'S10'],
            ['.', 'S11', 'S12'],]

    seats = [Seat(1, True, 2), Seat(2, True, 0),
             Seat(3, True, 2), Seat(4, True, 0),
             Seat(5, True, 2), Seat(6, True, 0),
             Seat(7, True, 2), Seat(8, True, 0),
             Seat(9, True, 2), Seat(10, True, 0),
             Seat(11, True, 2), Seat(12, True, 0)]

    carriage = Cariage(0, {}, seats, look)

    write_to_file_carriage(carriage)

    look2 = [['.', 'S1', 'S2'],
             ['.', 'T', 'T'],
             ['.', 'S3', 'S4'],
             ['.', 'S5', 'S6'],
             ['.', 'T', 'T'],
             ['.', 'S7', 'S8'],]

    seats1 = [
        Seat(1, True, 2, table=True), Seat(2, True, 0, table=True),
        Seat(3, True, 2, table=True), Seat(4, True, 0, table=True),
        Seat(5, True, 2, table=True), Seat(6, True, 0, table=True),
        Seat(7, True, 2, table=True), Seat(8, True, 0, table=True)
    ]

    carriage1 = Cariage(1, {}, seats1, look2)
    write_to_file_carriage(carriage1)



    look2 = [['S1', 'S2', 'S3'],
             ['S4', 'S5', 'S6'],
             ['S7', 'S8', 'S9'],
             ['S10', 'S11', 'S12'],
             ]

    seats1 = [
        Seat(1, False, 2, table=False), Seat(2, False, 1, table=False), Seat(3, False, 0, table=False),
        Seat(4, False, 2, table=False), Seat(5, False, 1, table=False), Seat(6, False, 0, table=False),
        Seat(7, False, 2, table=False), Seat(8, False, 1, table=False), Seat(9, False, 0, table=False),
        Seat(10, False, 2, table=False), Seat(11, False, 1, table=False), Seat(12, False, 0, table=False)

    ]

    carriage1 = Cariage(2, {}, seats1, look2)
    write_to_file_carriage(carriage1)