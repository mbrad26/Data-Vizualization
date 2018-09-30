import pygal
from die import Die

d_1 = Die()
d_2 = Die()

results = []
for i in range(100):
    result = d_1.roll() + d_2.roll()
    results.append(result)

print(results)

frequencies = []
max_result = d_1.num_sides + d_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()

hist.title = "Rolling 2 D6 - 100 times"
hist.x_labels = [x + 1 for x in range(1, max_result)]
hist.x_title = "Values"
hist.y_title = "Frequency of Value"

hist.add('2D6',frequencies)
hist.render_to_file('2_die_visual.svg')
