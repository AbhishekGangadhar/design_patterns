from typing import Type

from behavioral.strategy.fly_strategy import IFlyStrategy
from behavioral.strategy.quack_strategy import IQuackStrategy
from behavioral.strategy.display_strategy import IDisplayStrategy


class Duck:
    def __init__(self, fly_strategy: IFlyStrategy, quack_strategy: IQuackStrategy, display_strategy: IDisplayStrategy):
        self.fly_strategy = fly_strategy
        self.quack_strategy = quack_strategy
        self.display_strategy = display_strategy

    def execute_fly(self):
        return self.fly_strategy.fly()

    def execute_quack(self):
        return self.quack_strategy.quack()

    def execute_display(self):
        return self.display_strategy.display()
