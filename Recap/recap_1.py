import matplotlib.pyplot as plt

range_5000 = list(range(501))
cube_5000 = [x**3 for x in range_5000]

plt.figure(figsize=(10, 6))
plt.plot(cube_5000, c='blue', linewidth=10)
plt.title('First 5 number\'s cube', fontsize=26)
plt.xlabel('Numbers', fontsize=14)
plt.ylabel('Cubes', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()