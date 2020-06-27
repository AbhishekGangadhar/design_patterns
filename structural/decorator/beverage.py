from abc import ABC, abstractmethod


class IBeverage(ABC):
    @abstractmethod
    def get_cost(self) -> int:
        pass


class Coffee(IBeverage):
    def get_cost(self) -> int:
        return 3


class Espresso(IBeverage):
    def get_cost(self) -> int:
        return 4
