import matplotlib.pyplot as plt
from random_walk import RandomWalk


rw = RandomWalk(15000)
rw.generate_walk()

plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Blues, edgecolors='none', s=5)
plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=55)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=55)
plt.show()
plt.savefig('images/random_walk.png', bbox_inches='tight')

