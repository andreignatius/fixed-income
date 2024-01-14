import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from forward_swap_rate import calculate_forward_rate

# Load the OIS data from the CSV file
irs_data_path = '../data/IRS_Data.csv'
irs_data = pd.read_csv(irs_data_path)

# Convert Tenor to years and Rate to decimal
tenor_conversion = {'6m': 0.5, '1y': 1, '2y': 2, '3y': 3, '4y': 4, '5y': 5, '7y': 7, '10y': 10, '15y': 15, '20y': 20, '30y': 30}
irs_data['Tenor'] = irs_data['Tenor'].map(tenor_conversion)
irs_data['Rate'] = irs_data['Rate'].str.rstrip('%').astype('float') / 100  # Convert percentage to decimal

# Adjusting for semi-annual payments and 30/360 day count convention

# # The first discount factor remains the same (for 6-month tenor)
# discount_factors = {0.5: np.exp(-irs_data.iloc[0]['Rate'] * 0.5)}
# print("discount_factors0: ", discount_factors)

# # annual simplified
# # Bootstrapping discount factors for each tenor
# for index, row in irs_data.iloc[1:].iterrows():
#     tenor = row['Tenor']
#     rate = row['Rate']
#     print("check discount_factors: ", discount_factors)
#     # Calculate the present value of the fixed leg
#     pv_fixed_leg = sum([rate * discount_factors[t] for t in discount_factors if t < tenor])
#     print("pv_fixed_leg: ", pv_fixed_leg)
#     print("rate: ", rate)
#     print("tenor: ", tenor)
#     # Calculate the discount factor for the current tenor (adjust it to equate to 1 with the fixed leg)
#     discount_factors[tenor] = (1 - pv_fixed_leg) / (1 + rate)  # Simplified calculation

# Initialize the discount factors with the first known tenor from IRS data
discount_factors = {0.5: 1 / (1 + irs_data.iloc[0]['Rate'] * 0.5)}

# Bootstrapping discount factors for each tenor
for index, row in irs_data.iloc[1:].iterrows():
    tenor = row['Tenor']
    rate = row['Rate']
    num_payments = int(tenor * 2)  # Number of semi-annual periods

    # Calculate the present value of the fixed leg for each payment up to the current tenor
    pv_fixed_leg = 0
    for payment in range(1, num_payments):
        t_payment = payment * 0.5  # Semi-annual period
        # Calculate the present value of the fixed leg up to this payment
        pv_fixed_leg += (rate / 2) * discount_factors.get(t_payment, 0)

    # The last payment's discount factor is calculated and added to the dictionary
    # This is the missing piece from the previous code
    last_payment_df = (1 - pv_fixed_leg) / (1 + rate / 2)
    discount_factors[tenor] = last_payment_df
    pv_fixed_leg += (rate / 2) * last_payment_df

# Ensure the discount_factors dictionary is ordered by tenor
discount_factors = dict(sorted(discount_factors.items()))
print("discount_factors1: ", discount_factors)

# Convert discount factors to a DataFrame for plotting
df_plot = pd.DataFrame(list(discount_factors.items()), columns=['Tenor', 'Discount Factor'])
df_plot = df_plot.sort_values(by='Tenor')

# Plotting the LIBOR Discount Curve
plt.figure(figsize=(14, 7))
plt.plot(df_plot['Tenor'], df_plot['Discount Factor'], marker='o', label='LIBOR Discount Factors')

# Example usage - assuming df_plot contains the tenors and discount factors
# Let's calculate the 1y×1y forward rate as an example
print("check df_plot: ", df_plot)
forward_rate_1y1y = calculate_forward_rate(df_plot, 1, 2)
print(f"1y×1y forward rate: {forward_rate_1y1y:.2%}")

# Setting the plot details
plt.title('LIBOR Discount Curve')
plt.xlabel('Maturity (Years)')
plt.ylabel('Discount Factor')
plt.grid(True)
plt.legend()
plt.show()

