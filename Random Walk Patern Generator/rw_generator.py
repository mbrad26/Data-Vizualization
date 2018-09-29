import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:

    rw = RandomWalk(1500)
    rw.generate_walk()

    plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)
    plt.show()

    user_input = input('Generate new pattern?(y/n): ')
    if user_input == 'n':
        break