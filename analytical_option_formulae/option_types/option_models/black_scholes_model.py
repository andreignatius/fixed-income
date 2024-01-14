"""
Authors     : Andre Lim & Joseph Adhika
Tests       : option_types.test_option_models.test_black_76_model
Description : uses lognormal distribution of returns, strictly prices non-zero values
"""
import numpy as np
from scipy.stats import norm

from .abstract_option_model import AbstractOptionModel


class AbstractBlackScholesModel(AbstractOptionModel):
    """
    A base class used to model Black-Scholes option model
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
        self.d2 = self._calculate_d2()
        self.discount_factor = np.exp(-self.r * self.T)

    def _calculate_d1(self) -> float:
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (
            self.sigma * np.sqrt(self.T)
        )

    def _calculate_d2(self) -> float:
        return self.d1 - self.sigma * np.sqrt(self.T)


class VanillaBlackScholesModel(AbstractBlackScholesModel):
    def calculate_call_price(self) -> float:
        return self.S * norm.cdf(self.d1) - self.K * self.discount_factor * norm.cdf(
            self.d2
        )

    def calculate_put_price(self) -> float:
        return self.K * self.discount_factor * norm.cdf(-self.d2) - self.S * norm.cdf(
            -self.d1
        )


class DigitalCashOrNothingBlackScholesModel(AbstractBlackScholesModel):
    def calculate_call_price(self) -> float:
        return self.discount_factor * norm.cdf(self.d2)

    def calculate_put_price(self) -> float:
        return self.discount_factor * norm.cdf(-self.d2)


class DigitalAssetOrNothingBlackScholesModel(AbstractBlackScholesModel):
    def calculate_call_price(self) -> float:
        return self.S * norm.cdf(self.d1)

    def calculate_put_price(self) -> float:
        return self.S * norm.cdf(-self.d1)
