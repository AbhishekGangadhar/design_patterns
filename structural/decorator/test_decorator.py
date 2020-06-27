import unittest
from unittest import TestCase

from structural.decorator.beverage import Coffee, Espresso
from structural.decorator.add_on import Hazelnut, Vanilla, Caramel


class TestDecoratorPattern(TestCase):
    def test(self):
        coffee_with_hazelnut = Hazelnut(Coffee())
        self.assertEqual(6, coffee_with_hazelnut.get_cost())

        espresso_with_vanilla_caramel = Vanilla(Caramel(Espresso()))
        self.assertEqual(7, espresso_with_vanilla_caramel.get_cost())

        espresso_with_double_hazelnut = Hazelnut(Hazelnut(Espresso()))
        self.assertEqual(10, espresso_with_double_hazelnut.get_cost())

        coffee_with_no_add_ons = Coffee()
        self.assertEqual(3, coffee_with_no_add_ons.get_cost())


if __name__ == '__main__':
    unittest.main()
