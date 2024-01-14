from abc import ABC, abstractmethod


class AbstractOptionModel(ABC):
    @abstractmethod
    def calculate_call_price(self) -> float:
        pass

    @abstractmethod
    def calculate_put_price(self) -> float:
        pass
