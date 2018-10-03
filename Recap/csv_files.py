import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = '../CSV File Vizualization/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    for x, y in enumerate(header):
        print(x,y)

    dates, maxV, minV = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        maxv = row[1]
        minv = row[3]

        dates.append(date)
        maxV.append(maxv)
        minV.append(minv)


fig = plt.figure(figsize=(10, 6))
plt.plot(dates, maxV, c='red')
# plt.plot(dates, minV, c='red')
fig.autofmt_xdate()

plt.show()