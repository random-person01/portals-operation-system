import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)


def main():
    # Plot the high temperatures.
    colour = input("Please enter a valid colour: ")
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c=colour)

    # Format plot.
    plt.title("Income", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Dollars (k)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
