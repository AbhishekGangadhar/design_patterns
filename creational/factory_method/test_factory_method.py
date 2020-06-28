import unittest
from unittest import TestCase
from creational.factory_method.animal_factory import AnimalFactory


class TestFactoryMethodPattern(TestCase):
    def test(self):
        animal = AnimalFactory.get_animal_from_name("Shark")
        self.assertEqual("Shark", animal.get_name())

        animal = AnimalFactory.get_animal_from_name("Dog")
        self.assertEqual("Dog", animal.get_name())

        animal = AnimalFactory.get_animal_from_name("Penguin")
        self.assertEqual("Penguin", animal.get_name())

        self.assertRaises(Exception, AnimalFactory.get_animal_from_name, "Cat")


if __name__ == '__main__':
    unittest.main()
