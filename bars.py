import json
import math


def load_data(my_json_path):
    try:
        with open(my_json_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('file not found!')
        exit()


def get_biggest_bar(data):
    return max(data, key=lambda x: x['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda x: x['SeatsCount'])


def get_closest_bar(data):
    return min(data, key=distance)


def distance(bar):
    bar_coordinates = bar['geoData']['coordinates']
    return math.sqrt((bar_coordinates[0] - my_coordinates[0]) ** 2 + (bar_coordinates[1] - my_coordinates[1]) ** 2)


def get_coordinates():
    coordinates = input('input your longitude: '), input('input your latitude: ')
    try:
        return list(map(float, coordinates))
    except ValueError:
        print('wrong coordinates!')
        exit()


def print_bar(bar, feature):
    print('The {feature} bar is "{name}" with {seats} seats'.format(name=bar['Name'],
                                                                    seats=bar['SeatsCount'],
                                                                    feature=feature))

if __name__ == '__main__':
    json_path = input('input data path: ')
    bars = load_data(json_path)
    biggest_bar = get_biggest_bar(bars)
    print_bar(biggest_bar, 'biggest')
    smallest_bar = get_smallest_bar(bars)
    print_bar(smallest_bar, 'smallest')
    my_coordinates = get_coordinates()
    closest_bar = get_closest_bar(bars)
    print_bar(closest_bar, 'closest')
