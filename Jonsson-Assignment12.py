# Brenda Jonsson 11/17/2022
# Assignment 12

# Code a Python program that makes a map that shows which parts of the world are affected by fires.

# Download active fire data from:
# https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data

# These files contain information about fires burning in different locations around the globe, including the
# latitude and longitude, and the brightness of each fire. Using the data processing work and the mapping work
# from chapter 16, make a map that shows which parts of the world are affected by fires.


# Start of program
# Install pandas and plotly packages first

from pandas import * # This is for feeding the data into lists
import csv # This is for checking out the column names

# Checking out the column names and indexing them for curiosity's sake
filename = 'MODIS_C6_1_USA_contiguous_and_Hawaii_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Feeding the columns into lists that we can plot on a map
data = read_csv("MODIS_C6_1_USA_contiguous_and_Hawaii_7d.csv")

lats = data['latitude'].tolist()
lons = data['longitude'].tolist()
brightness = data['brightness'].tolist()

# This is just for cmax down below to get the brightness gradient working well
def max_value(list):
    # set first element as max
    max = list[0]
    for i in list:
        # check if the current element is greater than max
        if i > max:
            max = i
    return max

brightness_max = max_value(brightness)

# Building a world map

import plotly.graph_objects as go
from plotly import offline # This is just for the very last line which shows the figure


# Map the fires
# Good article on this topic: https://plotly.com/python/scatter-plots-on-maps/

fig = go.Figure(data=go.Scattergeo(
        locationmode = 'USA-states',
        lon = lons,
        lat = lats,
        marker_color= brightness,
        marker = dict(
        cmax = brightness_max,
        colorbar_title="Brightness")
))

fig.update_layout(
        title = 'Fires in North America',
        geo_scope='north america'
    )

offline.plot(fig, filename="US_Fires.html")
