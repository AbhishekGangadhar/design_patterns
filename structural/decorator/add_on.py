from abc import ABC, abstractmethod
from structural.decorator.beverage import IBeverage


class AddOn(IBeverage, ABC):
    def __init__(self, beverage: IBeverage):
        self.beverage = beverage


class Caramel(AddOn):
    def get_cost(self) -> int:
        return self.beverage.get_cost() + 2


class Vanilla(AddOn):
    def get_cost(self) -> int:
        return self.beverage.get_cost() + 1


class Hazelnut(AddOn):
    def get_cost(self) -> int:
        return self.beverage.get_cost() + 3

