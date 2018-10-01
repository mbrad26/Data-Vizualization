import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pygal

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# plt.plot()
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.7)
plt.plot(dates, lows, c='blue', alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title('Title', fontsize=26)
plt.xlabel('', fontsize=14)
plt.ylabel('Temp (F)', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
fig.autofmt_xdate()
plt.savefig('images/plot_sitka_2014.png', bbox_inches='tight')
plt.show()

# plt.scatter()
fig = plt.figure(figsize=(10, 6))
plt.scatter(dates, highs, c='red', s=10)
plt.scatter(dates, lows, c='blue', s=10)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title('Title', fontsize=26)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temp (F)', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/scatter_sitka_2014.png', bbox_inches='tight')
plt.show()

# pygal.Line()
hist = pygal.Line()
hist.title = 'Title'
hist.x_labels = dates
hist.y_labels = highs
hist.y_labels = lows
hist.add('Highs', highs)
hist.add('Lows', lows)
hist.render_to_file('images/images_pygal_sitka_2014.svg')