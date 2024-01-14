import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the OIS data from the CSV file
irs_data_path = '../data/IRS_Data.csv'
irs_data = pd.read_csv(irs_data_path)

# Convert Tenor to years and Rate to decimal
tenor_conversion = {'6m': 0.5, '1y': 1, '2y': 2, '3y': 3, '4y': 4, '5y': 5, '7y': 7, '10y': 10, '15y': 15, '20y': 20, '30y': 30}
irs_data['Tenor'] = irs_data['Tenor'].map(tenor_conversion)
irs_data['Rate'] = irs_data['Rate'].str.rstrip('%').astype('float') / 100  # Convert percentage to decimal

# Adjusting for semi-annual payments and 30/360 day count convention

# The first discount factor remains the same (for 6-month tenor)
discount_factors = {0.5: np.exp(-irs_data.iloc[0]['Rate'] * 0.5)}
print("discount_factors0: ", discount_factors)

# annual simplified
# Bootstrapping discount factors for each tenor
for index, row in irs_data.iloc[1:].iterrows():
    tenor = row['Tenor']
    rate = row['Rate']
    print("check discount_factors: ", discount_factors)
    # Calculate the present value of the fixed leg
    pv_fixed_leg = sum([rate * discount_factors[t] for t in discount_factors if t < tenor])
    print("pv_fixed_leg: ", pv_fixed_leg)
    print("rate: ", rate)
    print("tenor: ", tenor)
    # Calculate the discount factor for the current tenor (adjust it to equate to 1 with the fixed leg)
    discount_factors[tenor] = (1 - pv_fixed_leg) / (1 + rate)  # Simplified calculation

print("discount_factors1: ", discount_factors)

# Convert discount factors to a DataFrame for plotting
df_plot = pd.DataFrame(list(discount_factors.items()), columns=['Tenor', 'Discount Factor'])
df_plot = df_plot.sort_values(by='Tenor')

# Plotting the LIBOR Discount Curve
plt.figure(figsize=(14, 7))
plt.plot(df_plot['Tenor'], df_plot['Discount Factor'], marker='o', label='LIBOR Discount Factors')

# Setting the plot details
plt.title('LIBOR Discount Curve')
plt.xlabel('Maturity (Years)')
plt.ylabel('Discount Factor')
plt.grid(True)
plt.legend()
plt.show()

