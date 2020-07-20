from orgdata import OrgData


class Cli:
    def __init__(self):
        self.data = OrgData.load()
        self.total_points = 0
        self.personal_points = []

    def run(self):
        self.list_names()
        print("Please enter a person's name and their effort ratings, separated by spaces.")
        print("Add a comma to the end of each line to continue to the next person.")
        ratings = self.get_ratings()
        self.calculate_points(ratings)
        self.calculate_shares()

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
    
    def calculate_points(self, ratings):
        for rating in ratings:
            frags = rating.split(' ')
            name = frags[0]
            points = sum(list(map(int, frags[1:])))
            self.personal_points.append((name, points))
            self.total_points += points
    
    def calculate_shares(self):
        for person in self.personal_points:
            share = (person[1] / self.total_points) * 100
            print(f"{person[0]} -> {share}%")