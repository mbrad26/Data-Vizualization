import csv
from datetime import datetime
import pygal
import matplotlib.pyplot as plt

filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(f)

    # print(header)
    # for i, j in enumerate(reader):
    #     print(i, j)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# plt.plot()
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.7)
plt.plot(dates, lows, c='blue', alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title('Death Valley 2014- highs and lows', fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temp (F)', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/plot_death_valley.png', bbox_inches='tight')
plt.show()

# plt.scatter()
fig = plt.figure(figsize=(10, 6))
plt.scatter(dates, highs, c='red', edgecolors='none', s=10)
plt.scatter(dates, lows, c='blue', edgecolors='none', s=10)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)
plt.title('Death Valley 2014- highs and lows', fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temp (F)', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/scatter_death_valley.png', bbox_inches='tight')
plt.show()

# pygal.Line()
hist = pygal.Line()
hist.title = 'Death Valley 2014'
hist.x_labels = dates
hist.y_labels = highs
hist.y_labels = lows
hist.add('Highs', highs)
hist.add('Lows', lows)
hist.render_to_file('images/pygal_line_death_valley.svg')

