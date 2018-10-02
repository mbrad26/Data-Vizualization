import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pygal

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    # for index, name in enumerate(reader):
    #     print(index, name)

    dates, precips = [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        precip = int(float(row[19]))

        dates.append(date)
        precips.append(precip)

# plt.plot()
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, precips, c='red', alpha=.7)
plt.title('Sitka - Death Valley rainfall comparison -2014', fontsize=26)
plt.xlabel('', fontsize=14)
plt.ylabel('Precipitations', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
fig.autofmt_xdate()
plt.savefig('images/sitka_valley_rainfall_2014.png', bbox_inches='tight')
plt.show()

# pygal.Bar()
hist = pygal.Bar()
hist.title = 'Sitka - Death Valley rainfall comparison -2014'
hist.add('2014', precips)
hist.render_to_file('images/sitka_valley_rainfall_2014.svg')
