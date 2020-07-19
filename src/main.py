import os
import yaml


def read_file():
    filepath = os.getcwd() + '/data.yml'
    with open(filepath) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data