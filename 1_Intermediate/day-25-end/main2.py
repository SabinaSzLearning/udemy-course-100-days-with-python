import pandas
from pandas import unique

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_color = data["Primary Fur Color"]
values = unique(data_color)
output = {'Color': [], 'Number': []}

for ele in values[1:]:
        output['Color'].append(ele)
        output['Number'].append(int(data_color.str.count(ele).sum()))

print(output)

df = pandas.DataFrame(output)
print(df)
df.to_csv("Output.csv")