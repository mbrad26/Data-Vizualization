import matplotlib.pyplot as plt


numbers = list(range(100))
squares = [x**2 for x in numbers]
cubes = [x**3 for x in numbers]

plt.figure(figsize=(10, 6))

plt.plot(squares, linewidth=5)
plt.plot(cubes, linewidth=5)

plt.title('Squares Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=24)

plt.tick_params(axis='both', labelsize=14)
plt.show()