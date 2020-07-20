from orgdata import OrgData


class Cli:
    def __init__(self):
        self.data = OrgData.load()

    def run(self):
        self.list_names()
        print("Please enter a person's name and their effort ratings, separated by spaces.")
        print("Add a comma to the end of each line to continue to the next person.")
        ratings = self.get_ratings()
        print(ratings)

    def list_names(self):
        text = 'People: '
        for (i, person) in enumerate(self.data.people):
            text += person['name']
            if i < len(self.data.people) - 1:
                text += ' | '
        print(text)
    
    def get_ratings(self):
        ratings = []
        while True:
            input_line = input('<- ')
            ratings.append(input_line.replace(',', ''))
            if not input_line.endswith(','):
                break
        return ratings