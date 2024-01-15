import pandas as pd

ois_data = pd.read_csv("../data/OIS_Data.csv")
# print(ois_data.head())

# use dict comprehension?
tenor_mapping = {
    "6m": 0.5,
    "1y": 1,
    "2y": 2,
    "3y": 3,
    "4y": 4,
    "5y": 5,
    "7y": 7,
    "10y": 10,
    "15y": 15,
    "20y": 20,
    "30y": 30,
}
# oh there is a series.map
ois_data["Tenor"] = ois_data["Tenor"].map(tenor_mapping)
# rate to dec values
ois_data["Rate"] = ois_data["Rate"].str.strip("%").astype(float) / 100.0

print(ois_data)
