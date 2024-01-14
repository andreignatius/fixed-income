from .abstract_option_type import AbstractOption
from .option_models.bachelier_model import *
from .option_models.black_76_model import *
from .option_models.black_scholes_model import *
from .option_models.displaced_diffusion_model import *


class DigitalAssetOrNothingOption(AbstractOption):
    def black_scholes_model(
        self, S: float, K: float, r: float, sigma: float, T: float
    ) -> AbstractBlackScholesModel:
        return DigitalAssetOrNothingBlackScholesModel(S, K, r, sigma, T)

    def bachelier_model(
        self, S: float, K: float, r: float, sigma: float, T: float
    ) -> AbstractBachelierModel:
        return DigitalAssetOrNothingBachelierModel(S, K, r, sigma, T)

    def black_76_model(
        self, S: float, K: float, r: float, sigma: float, T: float
    ) -> AbstractBlack76Model:
        return DigitalAssetOrNothingBlack76Model(S, K, r, sigma, T)

    def displaced_diffusion_model(
        self, S: float, K: float, r: float, sigma: float, T: float, beta: float
    ) -> AbstractDisplacedDiffusionModel:
        return DigitalAssetOrNothingDisplacedDiffusionModel(S, K, r, sigma, T, beta)
