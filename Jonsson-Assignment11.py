# Brenda Jonsson 11/13/2022
# Assignment 11

# Program Requirements

# Code a Python program that uses matplotlib to create a scatter chart. The scatter chart should display the high
# and low temperatures for each day of one month in a town your choice.

# •	Gather the high and low data from a weather website (e.g. AccuWeather, WeatherChannel, Wunderground, etc)
#   for a month in 2021 for a town of your choice.
# •	Create lists to store your data (For this assignment, you can just hand enter the data. You do not have to
#   read it from a file, use an API or do screen scraping.)
# •	Create a scatter chart. Make your high values in one color and your low values in another color
# •	Include a title
# •	Include x and y axis titles
# •	Have the chart displayed and also saved to a file

import matplotlib.pyplot as plt

#Data from weather.com
high_temperatures = [50, 45, 43, 58, 50, 44, 43, 41, 45, 46, 47, 50, 49, 51, 53, 50, 51, 48, 45,
                     46, 49, 52, 49, 50, 50, 48, 47, 49, 49, 48]
low_temperatures = [39, 37, 40, 41, 39, 36, 34, 31, 35, 34, 33, 34, 36, 35, 34, 25, 31, 30, 34,
                    39, 42, 42, 42, 43, 42, 41, 39, 38, 38, 38]

#The x and y axes must be equal
x = [*range(1, len(high_temperatures) + 1)]

plt.scatter(x, high_temperatures, s=10, c='red')
plt.scatter(x, low_temperatures, s=10, c='blue')

#Labels
plt.title("High and Low Temperatures in Seattle, December 2021", fontsize=14)
plt.xlabel("Date in December", fontsize=12)
plt.ylabel("Temperature in Degrees Fahrenheit", fontsize=12)

#Save the graph
plt.savefig('seattletemps.png', bbox_inches='tight')

#Show the graph
plt.show()