import pygal
import matplotlib.pyplot as plt
from random_walk import RandomWalk


rw = RandomWalk(1500)
rw.generate_walk()

# plt.scatter()
plt.figure(figsize=(10, 6))
plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Blues, edgecolors='none', s=5)
plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=55)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=55)
plt.show()
plt.savefig('images/random_walk.png', bbox_inches='tight')

# pygal.Bar()
hist = pygal.Bar()
hist.title = 'Random Walk'
hist.x_labels = rw.x_values
hist.x_title = 'x Values'
hist.y_title = 'y Values'
hist.add('RW', rw.y_values)
hist.render_to_file('images/pygal_random_walk.svg')
