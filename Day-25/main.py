import pandas

data = pandas.read_csv("./2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray = data[data["Primary Fur Color"] == "Gray"]
black = data[data["Primary Fur Color"] == "Black"]
red = data[data["Primary Fur Color"] == "Cinnamon"]

gray_count = len(gray)
black_count = len(black)
red_count = len(red)

data_dict = {
    "Fur Color": ["Gray", "Black", "Red"],
    "Count": [gray_count, black_count, red_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Modified-Squirrel-Data.csv")