import csv
from datetime import datetime
import matplotlib.pyplot as plt


def get_data(filename, dates, highs, lows):
    with open(filename) as f2:
        reader = csv.reader(f2)
        next(reader)
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
# Sitka
dates, highs, lows = [], [], []
get_data('sitka_weather_2014.csv', dates, highs, lows)

plt.plot(dates, highs, c='orange')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.3)

# Death Valley
dates, highs, lows = [], [], []
get_data('death_valley_2014.csv', dates, highs, lows)

plt.plot(dates, highs, c='red', alpha=.5)
plt.plot(dates, lows, c='blue', alpha=.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)

# Styling
plt.title('Title', fontsize=26)
plt.xlabel('', fontsize=14)
plt.ylabel('Temp', fontsize=14)
plt.ylim(0, 120)
fig.autofmt_xdate()
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/plot_sitka_valley.png', bbox_inches='tight')
plt.show()


