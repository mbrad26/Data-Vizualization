import pygal
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


die = Die(8)
die_1 = Die(8)


results = [die.roll() + die_1.roll() for x in range(1000)]

frequencies = [results.count(x) for x in range(2, 2 * die.sides + 1)]

# pygal.bar
hist = pygal.Bar()
hist.title = 'Rolling D6 - 1000'
hist.x_labels = [str(x) for x in range(2, 2 * die.sides + 1)]
hist.x_title = 'Sides'
hist.y_title = 'Frequency'
hist.add('D6', frequencies)
hist.render_to_file('recap_die_2d8.svg')
