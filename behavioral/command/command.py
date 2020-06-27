from abc import ABC, abstractmethod
from behavioral.command.number import Number


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass


class AddCommand(ICommand):
    def __init__(self, number: Number, val: int):
        self.number = number
        self.val = val

    def execute(self):
        result = self.number.get_number() + self.val
        self.number.set_number(result)

    def unexecute(self):
        result = self.number.get_number() - self.val
        self.number.set_number(result)


class SubtractCommand(ICommand):
    def __init__(self, number: Number, val: int):
        self.number = number
        self.val = val

    def execute(self):
        result = self.number.get_number() - self.val
        self.number.set_number(result)

    def unexecute(self):
        result = self.number.get_number() + self.val
        self.number.set_number(result)


class MultiplyCommand(ICommand):
    def __init__(self, number: Number, val: int):
        self.number = number
        self.val = val

    def execute(self):
        result = self.number.get_number() * self.val
        self.number.set_number(result)

    def unexecute(self):
        result = self.number.get_number() // self.val
        self.number.set_number(result)


class DivideCommand(ICommand):
    def __init__(self, number: Number, val: int):
        self.number = number
        self.val = val

    def execute(self):
        result = self.number.get_number() // self.val
        self.number.set_number(result)

    def unexecute(self):
        result = self.number.get_number() * self.val
        self.number.set_number(result)


class AddAndMultiplyCommand(ICommand):
    def __init__(self, number: Number, add_val: int, multiple_val: int):
        self.number = number
        self.add_val = add_val
        self.multiple_val = multiple_val

    def execute(self):
        result = (self.number.get_number() + self.add_val) * self.multiple_val
        self.number.set_number(result)

    def unexecute(self):
        result = (self.number.get_number() // self.multiple_val) - self.add_val
        self.number.set_number(result)
