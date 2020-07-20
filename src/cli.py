from orgdata import OrgData


class Cli:
    def __init__(self):
        self.data = OrgData.load()

    def run(self):
        self.list_names()

    def list_names(self):
        text = 'People: '
        for (i, person) in enumerate(self.data.people):
            text += person['name']
            if i < len(self.data.people) - 1:
                text += ' | '
        print(text)