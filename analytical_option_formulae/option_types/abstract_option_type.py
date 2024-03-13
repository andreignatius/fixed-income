from abc import ABC, abstractmethod

from .option_models.bachelier_model import AbstractBachelierModel
from .option_models.black_76_model import AbstractBlack76Model
from .option_models.black_scholes_model import AbstractBlackScholesModel
from .option_models.displaced_diffusion_model import \
    AbstractDisplacedDiffusionModel


class AbstractOption(ABC):
    @abstractmethod
    def black_scholes_model(self) -> AbstractBlackScholesModel:
        pass

    @abstractmethod
    def bachelier_model(self) -> AbstractBachelierModel:
        pass

    @abstractmethod
    def black_76_model(self) -> AbstractBlack76Model:
        pass

    @abstractmethod
    def displaced_diffusion_model(self) -> AbstractDisplacedDiffusionModel:
        pass
