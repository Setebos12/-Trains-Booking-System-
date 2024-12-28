import requests
from bs4 import BeautifulSoup


def clean_data_km(data):
    cleaned_data = data.strip()
    cleaned_data = cleaned_data.splitlines()[1]
    cleaned_data = cleaned_data.strip()

    return cleaned_data[:-3]


def clean_data(data):
    cleaned_data = data.strip()
    cleaned_data = ' '.join(cleaned_data.splitlines())
    cleaned_data = ' '.join(cleaned_data.split())
    return cleaned_data


def get_station_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('span', class_='item-label', string='Nazwa')
    station_name = name.find_next('strong', class_='item-value')

    addrress = soup.find('span', class_='item-label', string='Adres')
    station_addres = addrress.find_next('strong', class_='item-value').text
    cleaned_address = clean_data(station_addres)

    localization = soup.find('span', class_='item-label', string='Współrzędne GPS')
    gps = localization.find_next('strong', class_='item-value').text
    gps = clean_data(gps)
    gps = gps.split(' ')

    return station_name.text, cleaned_address, gps


def get_all_stations_info(url):
    response = requests.get(url)
    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    stations_info = []

    stations = soup.find_all('span', {'class': 'visuallyhidden', 'aria-hidden': 'true'})

    for station in stations:
        station_info = {}

        station_name_tag = station.find_next('span', lang="pl-PL")
        if station_name_tag:
            station_info['station'] = station_name_tag.get_text(strip=True)

        arrival_time_tag = station.find_parent().find('span', {'class': 'timeline__numbers-time__stop'})
        if arrival_time_tag:
            arrival_time = arrival_time_tag.get_text(strip=True)
            station_info['arrival_time'] = arrival_time[8:13]

        departure_time_tag = station.find_parent().find('span', {'class': 'timeline__numbers-time__start'})
        if departure_time_tag:
            departure_time = departure_time_tag.get_text(strip=True)
            station_info['departure_time'] = departure_time[6:11]

        platform_and_track_tag = station.find_parent().find('p', {'class': 'timeline__content-platform'})
        if platform_and_track_tag:
            station_info['platform'] = platform_and_track_tag.get_text(strip=True)

        distance_name = station.find_next('p', class_= "timeline__numbers-km txlc")
        if distance_name:
            station_info['distance'] = clean_data_km(distance_name.text)

        if station_info:
            stations_info.append(station_info)

    return stations_info
