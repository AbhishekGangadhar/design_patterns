from abc import ABC


class IAnimal(ABC):
    def get_name(self) -> str:
        return self.__class__.__name__


class Dog(IAnimal):
    pass


class Shark(IAnimal):
    pass


class Penguin(IAnimal):
    pass

