import pytest

from option_types.option_models.displaced_diffusion_model import *

# Example:
S = 1997.271928  # Stock price today
K = 2100  # Strike price
T = 0.08493  # Time until expiry (in years)
r = 0.051342  # Risk-free rate
sigma = 0.35  # Volatility
beta = 1  # displaced diffusion parameter. if DDM = 1 then should equal Black76


vanillaDDM = VanillaDisplacedDiffusionModel(S, K, r, sigma, T, beta)


# Values taken from here, the results is slightly different because discounting is slightly different
# https://www.lme.com/en/trading/contract-types/options/black-scholes-76-formula


# This will give you the price of digital cash call and put options using the Displaced Diffusion formula.
def test_vanilla_call_price():
    EST_OPTION_VALUE = 44.57817
    tolerance = 0.00001
    call_price = vanillaDDM.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_vanilla_put_price():
    EST_OPTION_VALUE = 138.1692
    tolerance = 0.00001
    put_price = vanillaDDM.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalCashOrNothingDDM = DigitalCashOrNothingDisplacedDiffusionModel(
    S, K, r, sigma, T, beta
)


# This will give you the price of digital cash call and put options using the Displaced Diffusion formula.
def test_digital_cash_or_nothing_call_price():
    EST_OPTION_VALUE = 0.307206
    tolerance = 0.00001
    call_price = digitalCashOrNothingDDM.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_cash_or_nothing_put_price():
    EST_OPTION_VALUE = 0.688443
    tolerance = 0.00001
    put_price = digitalCashOrNothingDDM.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalAssetOrNothingDDM = DigitalAssetOrNothingDisplacedDiffusionModel(
    S, K, r, sigma, T, beta
)


# This will give you the price of digital asset call and put options using the Displaced Diffusion formula.
def test_digital_asset_or_nothing_call_price():
    EST_OPTION_VALUE = 689.71
    tolerance = 0.00001
    call_price = digitalAssetOrNothingDDM.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_asset_or_nothing_put_price():
    EST_OPTION_VALUE = 1307.561
    tolerance = 0.00001
    put_price = digitalAssetOrNothingDDM.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)
