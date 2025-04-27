# with open("weather_data.csv", mode = 'r') as file:
#     text = file.readlines()
#     print(text[0])

# import csv
#
# with open("weather_data.csv", mode = 'r') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row[1])

import pandas

from numpy.ma.extras import average

data = pandas.read_csv("weather_data.csv")
data = data["temp"].max()
print(data)

