from Routes.Route import Route, NotDateTimeDatError
from datetime import datetime
import pytest


def test_create_Route():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    route = Route("Warszawa Centralna", "Kraków", data1, data2, 300)

    assert route.starting_station() == "Warszawa Centralna"
    assert route.destination_station() == "Kraków"
    assert route.arrival_time() == data1
    assert route.departure_time() == data2
    assert route.is_booked() is False


def test_create_Route_no_datatime():
    data1 = (2024, 12, 29, 20, 30)
    data2 = (2024, 12, 29, 17, 30)
    with pytest.raises(NotDateTimeDatError):
        Route("Warszawa Centralna", "Kraków", data1, data2, 300)


def test_create_Route_negative_time():
    data1 = datetime(2024, 12, 29, 20, 30)
    data2 = datetime(2024, 12, 29, 17, 30)
    with pytest.raises(ValueError):
        Route("Warszawa Centralna", "Kraków", data2, data1, 300)