import pandas as pd

# read data
ois_data = pd.read_csv("../data/OIS_Data.csv")
irs_data = pd.read_csv("../data/IRS_Data.csv")
ois_data.columns = map(str.lower, ois_data.columns)
irs_data.columns = map(str.lower, irs_data.columns)

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

# OIS processing
ois_data["tenor"] = ois_data["tenor"].map(tenor_mapping)
ois_data["rate"] = ois_data["rate"].str.strip("%").astype(float) / 100.0

# IRS processing
irs_data["tenor"] = irs_data["tenor"].map(tenor_mapping)
irs_data["rate"] = irs_data["rate"].str.strip("%").astype(float) / 100.0

# check data
print(irs_data)

# get DF-OIS
ois_data["disc_factor"] = 1 / (1 + ois_data["tenor"] * ois_data["rate"])
print(ois_data)

# now try IRS
# just the libor rate
disc_6mlibor = 1 / (1 + irs_data.loc[0][0] * irs_data.loc[0][2])
# ada caranya ngga ya
