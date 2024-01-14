import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the OIS data from the CSV file
ois_data_path = '../data/OIS_Data.csv'
ois_data = pd.read_csv(ois_data_path)

# Convert Tenor to years and Rate to decimal
tenor_conversion = {'6m': 0.5, '1y': 1, '2y': 2, '3y': 3, '4y': 4, '5y': 5, '7y': 7, '10y': 10, '15y': 15, '20y': 20, '30y': 30}
ois_data['Tenor'] = ois_data['Tenor'].map(tenor_conversion)
ois_data['Rate'] = ois_data['Rate'].str.rstrip('%').astype('float') / 100  # Convert percentage to decimal

# print(ois_data['Rate'])

# Calculate the discount factors using the continuous compounding formula
ois_data['Discount Factor'] = np.exp(-ois_data['Rate'] * ois_data['Tenor'])

# Plot the OIS Discount Curve
plt.figure(figsize=(14, 7))
plt.plot(ois_data['Tenor'], ois_data['Discount Factor'], marker='o', label='OIS Discount Factors')

# Setting the x-axis to start from 0 and extend to the maximum tenor plus a margin
plt.xlim(0, ois_data['Tenor'].max() + 1)  # Adding 1 year margin for better visibility

# Adding titles and labels
plt.title('OIS Discount Curve')
plt.xlabel('Maturity (Years)')
plt.ylabel('Discount Factor')
plt.grid(True)
plt.legend()
plt.show()
