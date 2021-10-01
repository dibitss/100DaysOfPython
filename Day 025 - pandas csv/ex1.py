import pandas

data = pandas.read_csv("/home/dibits/Repos/100DaysOfPython/Day 025/squirrel_data.csv")

count = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count(), data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count(), data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()]
}
print(count)

squirrel_count = pandas.DataFrame(count)
squirrel_count.to_csv("/home/dibits/Repos/100DaysOfPython/Day 025/squirrel_count.csv")