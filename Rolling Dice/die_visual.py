import pygal
import matplotlib.pyplot as plt
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

# pygal.bar
hist = pygal.Bar()
hist.title = 'Rolling Dice - D6 for 1000 times'
hist.x_labels = [x + 1 for x in range(die.num_sides)]
hist._x_title = 'Sides'
hist.y_title = 'Frequencies of Sides'
hist.add('D6', frequencies)
hist.render_to_file('images/pygal_d6.svg')

# plt.plot()
sides = [x + 1 for x in range(die.num_sides)]
plt.figure(figsize=(10, 6))
plt.plot(sides, frequencies, c='red', linewidth=5)
plt.title('Rolling Dice - D6 for 1000 times', fontsize=26)
plt.xlabel('Sides', fontsize=14)
plt.ylabel('Frequencies', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 7, 0, 300])
plt.savefig('images/plot_d6.png', bbox_inches='tight')
plt.show()

# plt.scatter()
sides = [x + 1 for x in range(die.num_sides)]
plt.figure(figsize=(10,6))
plt.scatter(sides, frequencies, c='red', edgecolors='none', s=50)
plt.title('Rolling Dice - D6 for 1000 times', fontsize=26)
plt.xlabel('Values', fontsize=14)
plt.ylabel('Frequencies', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 7, 0, 300])
plt.savefig('images/scatter_d6.png', bbox_inches='tight')
plt.show()