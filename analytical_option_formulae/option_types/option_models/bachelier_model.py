"""
Authors     : Dylan Loo & Sarah Yin
Tests       : option_types.test_option_models.test_bachelier_model
Description : uses normal distribution of returns, allows for pricing of negative values
"""

import numpy as np
from scipy.stats import norm

from .abstract_option_model import AbstractOptionModel


class AbstractBachelierModel(AbstractOptionModel):
    """
    A base class used to model Bachelier model
    ...
    Parameters
    ----------
    S : float
        The current price of the underlying asset
    K : float
        The strike price of the options
    r : float
        Risk free interest rate (decimal)
    sigma : float
        Volatility
    T : float
        Maturity period (years)
    """

    def __init__(self, S: float, K: float, r: float, sigma: float, T: float):
        self.S = S
        self.K = K
        self.r = r
        self.sigma = sigma
        self.T = T

        self.d1 = self._calculate_d1()
        self.discount_factor = np.exp(-self.r * self.T)

    def _calculate_d1(self):
        return (self.S - self.K) / (self.sigma * self.S * np.sqrt(self.T))


class VanillaBachelierModel(AbstractBachelierModel):
    def calculate_call_price(self) -> float:
        call_price = self.discount_factor * (
            ((self.S - self.K) * norm.cdf(self.d1))
            + self.S * self.sigma * np.sqrt(self.T) * norm.pdf(self.d1)
        )
        return call_price

    def calculate_put_price(self) -> float:
        put_price = self.discount_factor * (
            ((self.K - self.S) * norm.cdf(-self.d1))
            + self.S * self.sigma * np.sqrt(self.T) * norm.pdf(-self.d1)
        )
        return put_price


class DigitalCashOrNothingBachelierModel(AbstractBachelierModel):
    def calculate_call_price(self) -> float:
        call_price = self.discount_factor * norm.cdf(self.d1)
        return call_price

    def calculate_put_price(self) -> float:
        put_price = self.discount_factor * norm.cdf(-self.d1)
        return put_price


class DigitalAssetOrNothingBachelierModel(AbstractBachelierModel):
    def calculate_call_price(self) -> float:
        call_price = (
            self.discount_factor
            * self.S
            * (norm.cdf(self.d1) + self.sigma * np.sqrt(self.T) * norm.pdf(self.d1))
        )
        return call_price

    def calculate_put_price(self) -> float:
        put_price = (
            self.discount_factor
            * self.S
            * (norm.cdf(-self.d1) - self.sigma * np.sqrt(self.T) * norm.pdf(-self.d1))
        )
        return put_price
