import unittest
from unittest import TestCase
from creational.singleton.logger import Logger


class TestSingletonPattern(TestCase):
    def test(self):
        self.assertRaises(Exception, Logger)

        logger_instance_1 = Logger.get_instance()
        logger_instance_2 = Logger.get_instance()
        self.assertIs(logger_instance_1, logger_instance_2)


if __name__ == '__main__':
    unittest.main()
