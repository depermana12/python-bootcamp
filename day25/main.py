import pandas as pd

raw_data = pd.read_csv("Squirrel_Census_Central_Park_2018.csv")

gray_count = len(raw_data[raw_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(raw_data[raw_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(raw_data[raw_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
