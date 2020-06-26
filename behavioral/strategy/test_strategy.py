import unittest
from unittest import TestCase
from behavioral.strategy.duck import Duck
from behavioral.strategy.quack_strategy import Quack, SqueakQuack, MuteQuack
from behavioral.strategy.fly_strategy import FlyWithWings, FlyNoWay
from behavioral.strategy.display_strategy import DisplayWithGraphics, DisplayWithText


class TestStrategyPattern(TestCase):
    def test(self):
        mallard_duck = Duck(fly_strategy=FlyWithWings(), quack_strategy=Quack(), display_strategy=DisplayWithGraphics())
        self.assertEqual("Executing FlyWithWings strategy", mallard_duck.execute_fly())
        self.assertEqual("Executing Quack strategy", mallard_duck.execute_quack())
        self.assertEqual("Executing DisplayWithGraphics strategy", mallard_duck.execute_display())

        redhead_duck = Duck(fly_strategy=FlyWithWings(), quack_strategy=MuteQuack(), display_strategy=DisplayWithGraphics())
        self.assertEqual("Executing FlyWithWings strategy", redhead_duck.execute_fly())
        self.assertEqual("Executing MuteQuack strategy", redhead_duck.execute_quack())
        self.assertEqual("Executing DisplayWithGraphics strategy", redhead_duck.execute_display())

        rubber_duck = Duck(fly_strategy=FlyNoWay(), quack_strategy=SqueakQuack(), display_strategy=DisplayWithText())
        self.assertEqual("Executing FlyNoWay strategy", rubber_duck.execute_fly())
        self.assertEqual("Executing SqueakQuack strategy", rubber_duck.execute_quack())
        self.assertEqual("Executing DisplayWithText strategy", rubber_duck.execute_display())


if __name__ == '__main__':
    unittest.main()
