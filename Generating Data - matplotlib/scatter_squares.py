import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

plt.title('Square numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize='14')
plt.show()

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=10)

plt.title('Square numbers', fontsize=14)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.axis([0, 1100, 0, 1100000])

plt.show()


x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c=(0.1, 0.5, 0.4), edgecolors='none', s=10)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()


x = list(range(1, 1001))
y = [x**2 for x in x]

plt.scatter(x, y, c=x, cmap=plt.cm.Reds, edgecolor='none', s=10)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])
plt.show()
plt.savefig('images/square_plot_1.png', bbox_inches='tight')


x = list(range(1, 5001))
y = [x**3 for x in x]

plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolor='none', s=10)

plt.title('Cubic numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('images/ cube_numbers.png', bbox_inches='tight')
plt.show()














































