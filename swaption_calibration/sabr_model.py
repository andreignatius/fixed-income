import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analytical_option_formulae.option_types.option_models.sabr_model import SABRModel

from scipy.optimize import brentq

