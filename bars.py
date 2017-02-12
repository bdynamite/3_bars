import json
import math


def load_data(filepath):
    with open(filepath, 'r', encoding='windows-1251') as file:
        data = json.load(file)
        return data


def get_biggest_bar(data):
    print((data[-1]['Name'], data[-1]['SeatsCount']))


def get_smallest_bar(data):
    print((data[0]['Name'], data[0]['SeatsCount']))


def get_closest_bar(data, longitude, latitude):
    closest_bar = get_bar_params(data[0], longitude, latitude)
    for bar in data:
        bar_params = get_bar_params(bar, longitude, latitude)
        if bar_params[1] < closest_bar[1]:
            closest_bar = bar_params
    print(closest_bar)


def get_bar_params(bar, longitude, latitude):
    name = bar['Name']
    coordinates = (bar['geoData']['coordinates'])
    distance = math.sqrt(((float(coordinates[0]) - float(longitude)) ** 2 + (float(coordinates[1]) - float(latitude)) ** 2))
    return (name, distance)


if __name__ == '__main__':
    path = input('input data path: ')
    bars = load_data(path)
    sorted_bars = sorted(bars, key=lambda x: x['SeatsCount'])
    get_biggest_bar(sorted_bars)
    get_smallest_bar(sorted_bars)
    get_closest_bar(bars, input('input your longitude: '), input('input your latitude: '))


