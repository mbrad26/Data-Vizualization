import pygal
from die import Die

d_1 = Die(8)
d_2 = Die(8)

results = []
for i in range(100000):
    result = d_1.roll() + d_2.roll()
    results.append(result)
print(results)

frequencies = []
for value in range(2, 2 * d_1.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)


hist = pygal.Bar()
hist.title = "2 8 sided dice"
hist.x_labels = [x + 1 for x in range(1, 2 * d_1.num_sides)]
hist.x_title = 'Sides'
hist.y_title = 'Frequencies of Sides'

hist.add('2*D8', frequencies)
hist.render_to_file('2_8_sided_die.svg')
