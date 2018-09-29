import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    rw = RandomWalk(5000)
    rw.generate_walk()

    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    # plt.title('Random walk .plot - 5000', fontsize=24)
    # plt.xlabel('Value', fontsize=14)
    # plt.ylabel('Value', fontsize=14)
    # plt.tick_params(axis='both', which='major', labelsize=14)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('molecular_motion.png', bbox_inches='tight')

    plt.show()

    user_input = input('Generate new pattern?(y/n): ')
    if user_input == 'n':
        break