import json
import math
import os
import chardet


def load_data(my_json_path):
    if not os.path.exists(my_json_path):
        raise Exception("file not found!")
    encoding = code_detecter(filepath)
    with open(my_json_path, 'r', encoding=encoding) as file:
        return json.load(file)


def code_detecter(path_to_file_text):
    with open(path_to_file_text, 'rb') as source:
        lines = source.read()
        result = chardet.detect(lines)
        if result['encoding'] is None:
            raise Exception("Unknown encoding!")
        else:
            return result['encoding']


def get_biggest_bar(data):
    print('The biggest bar is "{}" with {} seats'.format(data[-1]['Name'], data[-1]['SeatsCount']))


def get_smallest_bar(data):
    print('The smallest bar is "{}" with {} seats'.format(data[0]['Name'], data[0]['SeatsCount']))


def get_closest_bar(data):

    try:
        longitude = float(input('input your longitude: '))
    except ValueError:
        longitude = None
    if longitude is None:
        print('wtf, dude?')

    try:
        latitude = float(input('input your latitude: '))
    except ValueError:
        latitude = None
    if latitude is None:
        print('wtf, dude?')

    closest_bar = get_bar_params(data[0], longitude, latitude)
    for bar in data:
        bar_params = get_bar_params(bar, longitude, latitude)
        if bar_params[1] < closest_bar[1]:
            closest_bar = bar_params
    print('The closest bar is "{}"'.format(closest_bar[0]))


def get_bar_params(bar, longitude, latitude):
    name = bar['Name']
    coordinates = (bar['geoData']['coordinates'])
    distance = math.sqrt(((float(coordinates[0]) - float(longitude)) ** 2
                          + (float(coordinates[1]) - float(latitude)) ** 2))
    return name, distance


if __name__ == '__main__':
    filepath = input('input data path: ')
    bars = load_data(filepath)
    sorted_bars = sorted(bars, key=lambda x: x['SeatsCount'])
    get_biggest_bar(sorted_bars)
    get_smallest_bar(sorted_bars)
    get_closest_bar(bars)
