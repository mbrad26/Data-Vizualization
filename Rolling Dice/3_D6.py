import pygal
import matplotlib.pyplot as plt
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

# pygal.bar()
hist = pygal.Bar()
hist.title = '3 D6 dice - 1000 times'
hist.x_labels = [x + 1 for x in range(2, 3 * d_1.num_sides)]
hist.x_title = 'Sides'
hist.y_title = 'Frequencies of sides'
hist.add('3D6', frequencies)
hist.render_to_file('images/pygal_3d6.svg')

sides = [x + 1 for x in range(2, 3 * d_1.num_sides)]
# plt.plot()
plt.figure(figsize=(10,6))
plt.plot(sides, frequencies, c='red', linewidth=5)
plt.title('3 D6 dice - 1000 times', fontsize=26)
plt.xlabel('Sides', fontsize=14)
plt.ylabel('Frequencies of Sides', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/plot_3d6.png', bbox_inches='tight')
plt.show()

# plt.scatter()
plt.figure(figsize=(10, 6))
plt.scatter(sides, frequencies, c='red', edgecolors='none', s=50)
plt.title('3 D6 dice - 1000 times', fontsize=26)
plt.xlabel('Sides', fontsize=14)
plt.ylabel('Frequencies of sides', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/scatter_3d6.png', bbox_inches='tight')
plt.show()
