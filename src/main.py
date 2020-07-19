import os
import yaml


class OrgData:
    def __init__(self, data):
        self.standings = data['standings']
        self.people = data['people']


def read_file():
    filepath = os.getcwd() + '/data.yml'
    with open(filepath) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return OrgData(data)