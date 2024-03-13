import pytest

from option_types.option_models.bachelier_model import *

# Example 1, S=K:
S = 100  # Stock price today
K = 100  # Strike price
T = 1  # Time until expiry (in years)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility

vanillaBachelier = VanillaBachelierModel(S, K, r, sigma, T)


# This will give you the price of European call and put options using the Bachelier formula.
def test_vanilla_call_price():
    EST_OPTION_VALUE = 7.58971
    tolerance = 0.0001
    call_price = vanillaBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_vanilla_put_price():
    EST_OPTION_VALUE = 7.58971
    tolerance = 0.0001
    put_price = vanillaBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalCashOrNothingBachelier = DigitalCashOrNothingBachelierModel(S, K, r, sigma, T)


# This will give you the price of digital cash call and put options using the Bachelier formula.
def test_digital_cash_or_nothing_call_price():
    EST_OPTION_VALUE = 0.47561
    tolerance = 0.0001
    call_price = digitalCashOrNothingBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_cash_or_nothing_put_price():
    EST_OPTION_VALUE = 0.47561
    tolerance = 0.0001
    put_price = digitalCashOrNothingBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalAssetOrNothingBachelier = DigitalAssetOrNothingBachelierModel(S, K, r, sigma, T)


# This will give you the price of digital asset call and put options using the Bachelier formula.
def test_digital_asset_or_nothing_call_price():
    EST_OPTION_VALUE = 55.15118
    tolerance = 0.0001
    call_price = digitalAssetOrNothingBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_asset_or_nothing_put_price():
    EST_OPTION_VALUE = 55.15118
    tolerance = 0.0001
    put_price = digitalAssetOrNothingBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


# Example 2, S>K:
S = 103  # Stock price today
K = 100  # Strike price
T = 1  # Time until expiry (in years)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility

vanillaBachelier = VanillaBachelierModel(S, K, r, sigma, T)


# This will give you the price of European call and put options using the Bachelier formula.
def test_vanilla_call_price():
    EST_OPTION_VALUE = 6.24809
    tolerance = 0.0001
    call_price = vanillaBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_vanilla_put_price():
    EST_OPTION_VALUE = 9.10178
    tolerance = 0.0001
    put_price = vanillaBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalCashOrNothingBachelier = DigitalCashOrNothingBachelierModel(S, K, r, sigma, T)


# This will give you the price of digital cash call and put options using the Bachelier formula.
def test_digital_cash_or_nothing_call_price():
    EST_OPTION_VALUE = 0.53068
    tolerance = 0.0001
    call_price = digitalCashOrNothingBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_cash_or_nothing_put_price():
    EST_OPTION_VALUE = 0.42054
    tolerance = 0.0001
    put_price = digitalCashOrNothingBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalAssetOrNothingBachelier = DigitalAssetOrNothingBachelierModel(S, K, r, sigma, T)


# This will give you the price of digital asset call and put options using the Bachelier formula.
def test_digital_asset_or_nothing_call_price():
    EST_OPTION_VALUE = 62.39548
    tolerance = 0.0001
    call_price = digitalAssetOrNothingBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_asset_or_nothing_put_price():
    EST_OPTION_VALUE = 51.05103
    tolerance = 0.0001
    put_price = digitalAssetOrNothingBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


# Example 3, S<K:
S = 100  # Stock price today
K = 103  # Strike price
T = 1  # Time until expiry (in years)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility

vanillaBachelier = VanillaBachelierModel(S, K, r, sigma, T)


# This will give you the price of European call and put options using the Bachelier formula.
def test_vanilla_call_price():
    EST_OPTION_VALUE = 6.24809
    tolerance = 0.0001
    call_price = vanillaBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_vanilla_put_price():
    EST_OPTION_VALUE = 9.10178
    tolerance = 0.0001
    put_price = vanillaBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalCashOrNothingBachelier = DigitalCashOrNothingBachelierModel(S, K, r, sigma, T)


# This will give you the price of digital cash call and put options using the Bachelier formula.
def test_digital_cash_or_nothing_call_price():
    EST_OPTION_VALUE = 0.41890
    tolerance = 0.0001
    call_price = digitalCashOrNothingBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_cash_or_nothing_put_price():
    EST_OPTION_VALUE = 0.53232
    tolerance = 0.0001
    put_price = digitalCashOrNothingBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)


digitalAssetOrNothingBachelier = DigitalAssetOrNothingBachelierModel(S, K, r, sigma, T)


# This will give you the price of digital asset call and put options using the Bachelier formula.
def test_digital_asset_or_nothing_call_price():
    EST_OPTION_VALUE = 49.39526
    tolerance = 0.0001
    call_price = digitalAssetOrNothingBachelier.calculate_call_price()
    assert call_price > 0
    assert call_price == pytest.approx(EST_OPTION_VALUE, tolerance)


def test_digital_asset_or_nothing_put_price():
    EST_OPTION_VALUE = 45.72767
    tolerance = 0.0001
    put_price = digitalAssetOrNothingBachelier.calculate_put_price()
    assert put_price > 0
    assert put_price == pytest.approx(EST_OPTION_VALUE, tolerance)
