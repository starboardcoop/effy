from orgdata import OrgData


class Cli:
    def __init__(self):
        self.data = OrgData.load()

    def run(self):
        self.list_names()
        print("Please enter a person's name and their effort ratings, separated by spaces.")
        print("Add a comma to the end of each line to continue to the next person.")

    def list_names(self):
        text = 'People: '
        for (i, person) in enumerate(self.data.people):
            text += person['name']
            if i < len(self.data.people) - 1:
                text += ' | '
        print(text)