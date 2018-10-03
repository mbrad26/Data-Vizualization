import pygal
from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


die_1 = Die()
die_2 = Die(12)
die_3 = Die(7)

results = [die_1.roll() + die_2.roll() + die_3.roll() for x in range(1000)]

t_sides = die_1.sides + die_2.sides + die_3.sides
frequencies = [results.count(x) for x in range(3, t_sides + 1)]


# pygal.Bar()

hist = pygal.Bar()
hist.title = 'Rolling 3 different sizes Dice - 1000'
hist.x_labels = [str(x) for x in range(3, t_sides + 1)]
hist.x_title = 'Sides'
hist.y_title = 'Frequency'
hist.add('3D', frequencies)
hist.render_to_file('recap_die_3dice.svg')
