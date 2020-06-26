from abc import ABCMeta, abstractmethod


class IQuackStrategy(metaclass=ABCMeta):
    @abstractmethod
    def quack(self) -> str:
        pass


class Quack(IQuackStrategy):
    def quack(self) -> str:
        return "Executing Quack strategy"


class SqueakQuack(IQuackStrategy):
    def quack(self) -> str:
        return "Executing SqueakQuack strategy"


class MuteQuack(IQuackStrategy):
    def quack(self) -> str:
        return "Executing MuteQuack strategy"

