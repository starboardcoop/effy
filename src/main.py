import os
import yaml


def read_file():
    filepath = os.getcwd() + '/data.yml'
    with open(filepath) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


def list_people(data):
    names = list(map(lambda p: p['name'], data['people']))
    message = 'People: '
    for name in names:
        message += name + '  '
    print(message)