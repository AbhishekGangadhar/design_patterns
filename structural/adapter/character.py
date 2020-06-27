from abc import ABC, abstractmethod


class ICharacter(ABC):
    @abstractmethod
    def attack(self) -> int:
        pass

    @abstractmethod
    def flee(self) -> int:
        pass

    @abstractmethod
    def chase(self) -> int:
        pass

