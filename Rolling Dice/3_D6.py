import pygal
from die import Die

d_1 = Die()
d_2 = Die()
d_3 = Die()

results = []
for i in range(1000):
    result = d_1.roll() + d_2.roll() + d_3.roll()
    results.append(result)
print(results)

frequencies = []
t_sides = 3 * d_1.num_sides
for value in range(3, t_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()
hist.title = "3 D6 dies"
hist.x_labels = [x + 1 for x in range(2, t_sides)]
hist._x_title = "Sides"
hist.y_title = "Frequency of Sides"

hist.add('3 D6', frequencies)
hist.render_to_file('3_D6.svg')