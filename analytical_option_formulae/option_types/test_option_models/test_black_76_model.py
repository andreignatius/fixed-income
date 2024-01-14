import pytest

from option_types.option_models.black_76_model import *

# Example:
S = 1997.271928  # Stock price today
K = 2100  # Strike price
T = 0.08493  # Time until expiry (in years)
r = 0.051342  # Risk-free rate
sigma = 0.35  # Volatility


vanillaBS76 = VanillaBlack76Model(S, K, r, sigma, T)


# This will give you the price of European call and put options using the Black76 formula.
def test_vanilla_call_price():
    EST_OPTION_VALUE = 44.57817
    tolerance = 0.00001
    call_price = vanillaBS76.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_vanilla_put_price():
    EST_OPTION_VALUE = 138.1692
    tolerance = 0.00001
    put_price = vanillaBS76.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalCashOrNothingBS76 = DigitalCashOrNothingBlack76Model(S, K, r, sigma, T)


# This will give you the price of digital cash call and put options using the Black76 formula.
def test_digital_cash_or_nothing_call_price():
    EST_OPTION_VALUE = 0.307206
    tolerance = 0.00001
    call_price = digitalCashOrNothingBS76.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_cash_or_nothing_put_price():
    EST_OPTION_VALUE = 0.688443
    tolerance = 0.00001
    put_price = digitalCashOrNothingBS76.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalAssetOrNothingBS76 = DigitalAssetOrNothingBlack76Model(S, K, r, sigma, T)


# This will give you the price of digital asset call and put options using the Black76 formula.
def test_digital_asset_or_nothing_call_price():
    EST_OPTION_VALUE = 689.71
    tolerance = 0.00001
    call_price = digitalAssetOrNothingBS76.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_asset_or_nothing_put_price():
    EST_OPTION_VALUE = 1307.561
    tolerance = 0.00001
    put_price = digitalAssetOrNothingBS76.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)
