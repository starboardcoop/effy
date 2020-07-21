import math
from blessings import Terminal
from orgdata import OrgData


class Cli:
    def __init__(self):
        self.data = OrgData.load()
        self.total_points = 0
        self.personal_points = []
        self.terminal = Terminal()

    def run(self):
        self.list_names()
        self.print_prompt("Please enter a person's name and their effort ratings, separated by spaces.")
        self.print_prompt("Add a comma to the end of each line to continue to the next person.")
        ratings = self.get_ratings()
        self.calculate_points(ratings)
        self.calculate_shares()

    def list_names(self):
        text = 'People: '
        for (i, person) in enumerate(self.data.people):
            text += self.terminal.bold_yellow(person['name'])
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
            standing = list(filter(lambda p: p['name'] == name, self.data.people))[0]['standing']
            multiplier = float(list(filter(lambda m: m['name'] == standing, self.data.standings))[0]['rate'])
            points = sum(list(map(int, frags[1:]))) * multiplier
            self.personal_points.append((name, points))
            self.total_points += points
    
    def calculate_shares(self):
        remainder = 0.0
        for person in self.personal_points:
            share = person[1] / self.total_points * 100
            truncated_share = math.trunc(share)
            remainder += share - truncated_share
            self.print_result(person[0], truncated_share)
        self.print_result('Remainder', remainder)
    
    def print_prompt(self, prompt):
        print(self.terminal.italic(prompt))

    def print_result(self, label, percentage):
        left = self.terminal.bold_yellow(f"{label}")
        right = self.terminal.bold_green(f"{percentage}%")
        print(left, '->', right)