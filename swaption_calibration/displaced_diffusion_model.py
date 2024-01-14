import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analytical_option_formulae.option_types.option_models.displaced_diffusion_model import VanillaDisplacedDiffusionModel

from scipy.optimize import brentq

def model_volatility(S, K, r, T, beta, market_price, option_type='call'):
    # Define a function that calculates the difference between model price and market price
    def price_diff(sigma):
        if option_type == 'call':
            model = VanillaDisplacedDiffusionModel(S, K, r, sigma, T, beta)
            return model.calculate_call_price() - market_price
        else:
            model = VanillaDisplacedDiffusionModel(S, K, r, sigma, T, beta)
            return model.calculate_put_price() - market_price

    # Use a root-finding algorithm to solve for sigma
    implied_vol = brentq(price_diff, 1e-6, 3)  # Example bounds, may need adjustment
    return implied_vol

