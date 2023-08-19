# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_in_fahrenheit = (monday_temp * 9/5) + 32
# print(monday_temp_in_fahrenheit)

# data_dict_students = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_students = pandas.DataFrame(data_dict_students)
# data_students.to_csv("scores.csv")
# print(data_students)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
