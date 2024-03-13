from .abstract_option_type import AbstractOption
from .option_models.bachelier_model import *
from .option_models.black_76_model import *
from .option_models.black_scholes_model import *
from .option_models.displaced_diffusion_model import *


class VanillaOption(AbstractOption):
    def black_scholes_model(
        self, S: float, K: float, r: float, sigma: float, T: float
    ) -> AbstractBlackScholesModel:
        return VanillaBlackScholesModel(S, K, r, sigma, T)

    def bachelier_model(
        self, S: float, K: float, r: float, sigma: float, T: float
    ) -> AbstractBachelierModel:
        return VanillaBachelierModel(S, K, r, sigma, T)

    def black_76_model(
        self, S: float, K: float, r: float, sigma: float, T: float
    ) -> AbstractBlack76Model:
        return VanillaBlack76Model(S, K, r, sigma, T)

    def displaced_diffusion_model(
        self, S: float, K: float, r: float, sigma: float, T: float, beta: float
    ) -> AbstractDisplacedDiffusionModel:
        return VanillaDisplacedDiffusionModel(S, K, r, sigma, T, beta)
