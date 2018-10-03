import matplotlib.pyplot as plt
from random import choice


class RW:
    def __init__(self, points=5000):
        self.points = points
        self.x_values = [0]
        self.y_values = [0]

    def fill_rw(self):
        while len(self.x_values) < self.points:
            x_direction = choice([1, -1])
            y_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            y_distance = choice([0, 1, 2, 3, 4])

            x_step = x_direction * x_distance
            y_step = y_direction * y_distance

            x_next = self.x_values[-1] + x_step
            y_next = self.y_values[-1] + y_step

            self.x_values.append(x_next)
            self.y_values.append(y_next)


rw = RW()
rw.fill_rw()

# plt.scatter()
plt.figure(figsize=(10, 6))
plt.scatter(rw.x_values, rw.y_values, c=list(range(rw.points)),
                cmap=plt.cm.Blues, edgecolors='none', s=10)
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.savefig('recap_rw_scatter.png')
plt.show()

# plt.plot()
plt.figure(figsize=(10, 6))
plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=.5)
plt.scatter(0, 0, c='green', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.savefig('recap_rw_plot.png')
plt.show()







