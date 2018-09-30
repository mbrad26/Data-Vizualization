import pygal
import matplotlib.pyplot as plt
from die import Die

d_1 = Die(8)
d_2 = Die(8)

results = []
for i in range(1000):
    result = d_1.roll() + d_2.roll()
    results.append(result)
print(results)

frequencies = []
for value in range(2, 2 * d_1.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)


# pygal.bar()
hist = pygal.Bar()
hist.title = '2 D8 sided dice - 1000 times'
hist.x_labels = [x + 1 for x in range(1, 2 * d_1.num_sides)]
hist.x_title = 'Sides'
hist.y_title = 'Frequencies of Sides'
hist.add('2 D8', frequencies)
hist.render_to_file('images/pygal_2d8.svg')

sides = [x + 1 for x in range(1, 2 * d_1.num_sides)]
# plt.plot()
plt.figure(figsize=(10, 6))
plt.plot(sides, frequencies, c='red', linewidth=5)
plt.title('2 D8 sided dice - 1000 times', fontsize=26)
plt.xlabel('Sides', fontsize=14)
plt.ylabel('Frequencies of Sides', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/plot_2d8.png', bbox_inches='tight')
plt.show()

# plt.scatter()
plt.figure(figsize=(10, 6))
plt.scatter(sides, frequencies, c='red', s=50)
plt.title('2 D8 sided dice - 1000 times', fontsize=26)
plt.xlabel('Sides', fontsize=14)
plt.ylabel('Frequencies of Sides', fontsize =14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/scatter_2d8.png', bbox_inches='tight')
plt.show()