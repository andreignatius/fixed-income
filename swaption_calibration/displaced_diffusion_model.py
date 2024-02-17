import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analytical_option_formulae.option_types.option_models.displaced_diffusion_model import VanillaDisplacedDiffusionModel
from analytical_option_formulae.option_types.option_models.black_76_model import VanillaBlack76Model

from bootstrap_swap_curve.forward_swap_rate import calculate_forward_rate

import pandas as pd
import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm

def calculate_market_price(implied_vol, F, K, T, r, option_type):
    black76_model = VanillaBlack76Model(F, K, r, implied_vol, T)
    print("call111: ", black76_model.calculate_call_price())
    if option_type == 'call':
        return black76_model.calculate_call_price()
    else:
        return black76_model.calculate_put_price()

# This function estimates the forward rate assuming it's the ATM strike plus ATM implied volatility.
def estimate_forward_rate(row):
    # Extract the expiry and tenor from the row
    expiry = row['Expiry']
    tenor = row['Tenor']
    atm_volatility = row['ATM'] / 100  # Assuming the ATM volatility is given in percentage

    # Convert expiry and tenor to years (assuming they are in a '1Y' string format)
    expiry_years = int(expiry[:-1])
    tenor_years = int(tenor[:-1])

    # For simplicity, let's assume the forward rate is the ATM volatility
    # This is a simplification and may not represent the actual forward rate in a real market scenario
    forward_rate = atm_volatility

    return forward_rate


# Load the swaption data from the CSV file
swaption_data_path = '../data/Swaption_Data.csv'
swaption_data = pd.read_csv(swaption_data_path)

tenor_conversion = {'1Y': 1, '2Y': 2, '3Y': 3, '4Y': 4, '5Y': 5, '7Y': 7, '10Y': 10}

def objective_function(params, market_data, r):
    sigma, beta = params
    total_squared_error = 0.0
    for _, row in market_data.iterrows():
        # Convert tenor and expiry using the conversion dictionary
        tenor_years = tenor_conversion[row['Tenor']]
        expiry_years = tenor_conversion[row['Expiry']]
        
        # Assume the forward rate is the ATM rate, and adjust by converting to a decimal
        # F = row['ATM'] / 10000  # Assuming ATM is basis points
        F = estimate_forward_rate(row)
        print("F: ", F)
        print("***")
        # Loop through all basis point shifts to calculate the error for each
        for basis_point_shift in [-200, -150, -100, -50, -25, 0, 25, 50, 100, 150, 200]:
            # Calculate the strike by adding/subtracting the basis point shift
            strike = F + basis_point_shift / 10000
            print("strike: ", strike)
            print("row: ", row)
            # Get the market implied volatility for the current basis point shift
            try:
                implied_vol = row[str(basis_point_shift)+'bps'] / 100  # Convert from percent to decimal
            except:
                implied_vol = row['ATM'] / 100
            print("implied_vol: ", implied_vol)
            print("111implied_vol: ", implied_vol, "F: ", F, "strike: ", strike, "tenor_years: ", tenor_years, "r: ", r)
            # Calculate the market price from the implied volatility
            market_price = calculate_market_price(implied_vol, F, strike, tenor_years, r, option_type='call')
            print("market_price: ", market_price)
            # Instantiate the displaced diffusion model with the estimated forward rate and parameters
            model = VanillaDisplacedDiffusionModel(F, strike, r, sigma, tenor_years, beta)
            
            # Calculate the model price
            model_price = model.calculate_call_price()  # Or put price if required
            print("model_price: ", model_price)
            # Compute squared error
            squared_error = (model_price - market_price) ** 2
            print("squared_error: ", squared_error)
            
            # Add to the total squared error
            total_squared_error += squared_error
            
    return total_squared_error

# Calibration
initial_guess = [0.2, 0.05]  # Initial guess for sigma and beta
r = 0.01  # Example risk-free rate
# result = minimize(objective_function, initial_guess, args=(swaption_data, r))
result = minimize(objective_function, initial_guess, args=(swaption_data, r), method='BFGS', options={'maxiter': 200}, tol=1e-6)


# Results
if result.success:
    calibrated_sigma, calibrated_beta = result.x
    print(f"Calibrated σ: {calibrated_sigma}, Calibrated β: {calibrated_beta}")
else:
    print("Calibration failed:", result.message)
