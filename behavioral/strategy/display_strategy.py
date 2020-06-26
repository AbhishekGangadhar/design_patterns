from abc import ABCMeta, abstractmethod


class IDisplayStrategy(metaclass=ABCMeta):
    @abstractmethod
    def display(self) -> str:
        pass


class DisplayWithGraphics(IDisplayStrategy):
    def display(self) -> str:
        return "Executing DisplayWithGraphics strategy"


class DisplayWithText(IDisplayStrategy):
    def display(self) -> str:
        return "Executing DisplayWithText strategy"
