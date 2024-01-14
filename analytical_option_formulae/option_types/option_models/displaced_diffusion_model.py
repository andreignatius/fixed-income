"""
Authors     : Andre Lim & Joseph Adhika
Tests       : option_types.test_option_models.test_displaced_diffusion_model.py
Description : Mark Rubinstein's Displaced Diffusion Model following lecture notes
"""
import numpy as np
from scipy.stats import norm

from .abstract_option_model import AbstractOptionModel


class AbstractDisplacedDiffusionModel(AbstractOptionModel):
    """
    Displaced diffusion is extension of Black76 with an additional parameter beta
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
    beta : float
        Displaced diffusion model parameter (0,1], but lecture notes say [0,1]
        https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=6976&context=lkcsb_research
    """

    def __init__(
        self, S: float, K: float, r: float, sigma: float, T: float, beta: float
    ):
        self.S = S
        self.K = K
        self.r = r
        self.sigma = sigma
        self.T = T
        self.beta = beta

        self.F = S * np.exp(r * T)
        self.adjusted_F = self.F / self.beta
        self.adjusted_K = self.K + ((1 - self.beta) / self.beta) * self.F
        self.adjusted_sigma = self.sigma * self.beta
        self.discount_factor = np.exp(-self.r * self.T)

        self.d1 = self._calculate_d1()
        self.d2 = self._calculate_d2()

    def _calculate_d1(self) -> float:
        return (
            np.log(self.adjusted_F / self.adjusted_K)
            + (0.5 * self.adjusted_sigma**2) * self.T
        ) / (self.adjusted_sigma * np.sqrt(self.T))

    def _calculate_d2(self) -> float:
        return (
            np.log(self.adjusted_F / self.adjusted_K)
            - (0.5 * self.adjusted_sigma**2) * self.T
        ) / (self.adjusted_sigma * np.sqrt(self.T))


class VanillaDisplacedDiffusionModel(AbstractDisplacedDiffusionModel):
    def calculate_call_price(self) -> float:
        return self.discount_factor * (
            self.adjusted_F * norm.cdf(self.d1) - self.adjusted_K * norm.cdf(self.d2)
        )

    def calculate_put_price(self) -> float:
        return self.discount_factor * (
            self.adjusted_K * norm.cdf(-self.d2) - self.adjusted_F * norm.cdf(-self.d1)
        )


class DigitalCashOrNothingDisplacedDiffusionModel(AbstractDisplacedDiffusionModel):
    def calculate_call_price(self) -> float:
        return self.discount_factor * norm.cdf(self.d2)

    def calculate_put_price(self) -> float:
        return self.discount_factor * norm.cdf(-self.d2)


class DigitalAssetOrNothingDisplacedDiffusionModel(AbstractDisplacedDiffusionModel):
    def calculate_call_price(self) -> float:
        return self.discount_factor * self.adjusted_F * norm.cdf(self.d1)

    def calculate_put_price(self) -> float:
        return self.discount_factor * self.adjusted_F * norm.cdf(-self.d1)
