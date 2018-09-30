import pygal
from die import Die

die = Die()

results = []
for i in range(1000):
    result = die.roll()
    results.append(result)

print(results)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print("\n" + str(frequencies))

hist = pygal.Bar()

hist.title = "Rolling Dice - D6 for 1000 times"
hist.x_labels = [x + 1 for x in range(die.num_sides)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')