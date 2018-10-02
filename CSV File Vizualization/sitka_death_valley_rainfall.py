import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pygal


def get_data(filename, dates, precips):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                precip = float(row[19])
            except ValueError:
                print(f'{date}: missing data!')
            else:
                dates.append(date)
                precips.append(precip)


fig = plt.figure(figsize=(10, 6))
# Sitka
dates, precips = [], []
get_data('sitka_weather_2014.csv', dates, precips)
plt.plot(dates, precips, c='blue', alpha=.7)
plt.fill_between(dates, precips, facecolor='blue', alpha=.1)

# Death Valley
dates, precips = [], []
get_data('death_valley_2014.csv', dates, precips)
plt.plot(dates, precips, c='red', alpha=.7)

plt.title('Sitka - Death Valley rainfall comparison -2014', fontsize=26)
plt.xlabel('', fontsize=14)
plt.ylabel('Precipitations', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
fig.autofmt_xdate()
plt.savefig('images/sitka_valley_rainfall_2014.png', bbox_inches='tight')
plt.show()

# # pygal.Bar()
# hist = pygal.Bar()
# hist.title = 'Sitka - Death Valley rainfall comparison -2014'
# hist.add('2014', precips)
# hist.render_to_file('images/sitka_valley_rainfall_2014.svg')
