import csv

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    print(reader)
    for index, name in enumerate(reader):
        print(index, name)

    dates, precips = [], []
    for row in reader:
        date = row[0]
        precip = row[19]

        dates.append(date)
        precips.append(precip)
