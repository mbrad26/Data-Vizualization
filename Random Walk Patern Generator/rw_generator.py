import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:

    rw = RandomWalk(15000)
    rw.generate_walk()

    plt.figure(figsize=(10, 6))

    points = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=points, cmap=plt.cm.Blues, edgecolors='none', s=5, linewidth=1)

    # plt.title('Random Walk Pattern - 50000 points', fontsize=24)
    # plt.xlabel('Value', fontsize=14)
    # plt.ylabel('Value', fontsize=14)
    # plt.tick_params(axis='both', which='major', labelsize=14)

    # plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)
    # plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)
    plt.scatter(0,0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('rw_pattern.png', bbox_inches='tight')
    plt.show()

    user_input = input('Generate new pattern?(y/n): ')
    if user_input == 'n':
        break

