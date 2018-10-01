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

# pygal.bar()
hist = pygal.Bar()
hist.title = 'Rolling 2 dice of different size - 1000 times'
hist.x_labels = [x + 1 for x in range(1, t_sides)]
hist.x_title = 'Sides'
hist.y_title = 'Frequencies of Sides'
hist.add('D6 D8', frequencies)
hist.render_to_file('images/pygal_d6d8.svg')

sides = [x + 1 for x in range(1, t_sides)]
# plt.plot()
plt.figure(figsize=(10, 6))
plt.plot(sides, frequencies, c='red', linewidth=5)
plt.title('Rolling 2 dice of different size - 1000 times', fontsize=26)
plt.xlabel('Sides', fontsize=14)
plt.ylabel('Frequencies of Sides', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/plot_d6d8.png', bbox_inches='tight')
plt.show()

# plt.scatter()
plt.figure(figsize=(10, 6))
plt.scatter(sides, frequencies, c='red', s=50)
plt.title('Rolling 2 dice of different size - 1000 times', fontsize=26)
plt.xlabel('Sides', fontsize=14)
plt.ylabel('Frequencies of Sides', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/scatter_d6d8.png', bbox_inches='tight')
plt.show()
