import pygal
import matplotlib.pyplot as plt
from die import Die

d_1 = Die()
d_2 = Die(8)

results = []
for i in range(1000):
    result = d_1.roll() + d_2.roll()
    results.append(result)
print(results)

frequencies = []
t_sides = d_1.num_sides + d_2.num_sides
for i in range(2, t_sides + 1):
    frequency = results.count(i)
    frequencies.append(frequency)
print(frequencies)


hist = pygal.Bar()

hist.title = "Rolling Dice of different sizes"
hist.x_labels = [x + 1 for x in range(1, t_sides)]
hist.x_title = "Sides"
hist.y_title = "Frequencies of Sides"

hist.add('D6 D10', frequencies)
hist.render_to_file('2_different_die.svg')

