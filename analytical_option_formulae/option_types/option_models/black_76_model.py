"""
Authors     : Eko Widianto
Tests       : option_types.test_option_models.test_black_76_model
Description : 
"""

import numpy as np
from scipy.stats import norm

from .abstract_option_model import AbstractOptionModel


class AbstractBlack76Model(AbstractOptionModel):
    """
    A base class used to model Black 76 option model
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

        self.F = self.S * np.exp(self.r * self.T)
        self.d1 = self._calculate_d1()
        self.d2 = self._calculate_d2()
        self.discount_factor = np.exp(-self.r * self.T)

    def _calculate_d1(self) -> float:
        return (np.log(self.F / self.K) + self.sigma**2 / 2 * self.T) / (
            self.sigma * np.sqrt(self.T)
        )

    def _calculate_d2(self) -> float:
        return self.d1 - self.sigma * np.sqrt(self.T)


class VanillaBlack76Model(AbstractBlack76Model):
    def calculate_call_price(self) -> float:
        return self.discount_factor * (
            self.F * norm.cdf(self.d1) - self.K * norm.cdf(self.d2)
        )

    def calculate_put_price(self) -> float:
        return self.discount_factor * (
            -self.F * norm.cdf(-self.d1) + self.K * norm.cdf(-self.d2)
        )


class DigitalCashOrNothingBlack76Model(AbstractBlack76Model):
    def calculate_call_price(self) -> float:
        return self.discount_factor * norm.cdf(self.d2)

    def calculate_put_price(self) -> float:
        return self.discount_factor * norm.cdf(-self.d2)


class DigitalAssetOrNothingBlack76Model(AbstractBlack76Model):
    def calculate_call_price(self) -> float:
        return self.discount_factor * self.F * norm.cdf(self.d1)

    def calculate_put_price(self) -> float:
        return self.discount_factor * self.F * norm.cdf(-self.d1)
