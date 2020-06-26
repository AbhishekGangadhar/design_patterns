from abc import ABCMeta, abstractmethod


class IFlyStrategy(metaclass=ABCMeta):
    @abstractmethod
    def fly(self) -> str:
        pass


class FlyWithWings(IFlyStrategy):
    def fly(self) -> str:
        return "Executing FlyWithWings strategy"


class FlyNoWay(IFlyStrategy):
    def fly(self) -> str:
        return "Executing FlyNoWay strategy"
