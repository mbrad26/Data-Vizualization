import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_1 = 'sitka_weather_2014.csv'
file_2 = 'death_valley_2014.csv'


with open(file_1) as f1:
    reader = csv.reader(f1)
    next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[1])
        low = int(row[3])
        dates.append(date)
        highs.append(high)
        lows.append(low)

with open(file_2) as f2:
    reader = csv.reader(f2)
    next(reader)
    dates_2, highs_2, lows_2 = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            dates_2.append(date)
            highs_2.append(high)
            lows_2.append(low)

# plt.plot()
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='black', alpha=.7)
plt.plot(dates, lows, c='green', alpha=.7)
plt.plot(dates_2, highs_2, c='red')
plt.plot(dates_2, lows_2, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)
plt.title('Title', fontsize=26)
plt.xlabel('', fontsize=14)
plt.ylabel('Temp', fontsize=14)
fig.autofmt_xdate()
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/plot_sitka_valley.png', bbox_inches='tight')
plt.show()


