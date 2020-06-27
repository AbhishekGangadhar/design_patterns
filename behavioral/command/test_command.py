import unittest
from unittest import TestCase

from behavioral.command.invoker import Invoker
from behavioral.command.number import Number
from behavioral.command.command import (
    AddCommand,
    SubtractCommand,
    MultiplyCommand,
    DivideCommand,
    AddAndMultiplyCommand
)


class TestCommandPattern(TestCase):
    def test(self):
        invoker = Invoker()
        number = Number(1)
        self.assertEqual(1, number.get_number())

        invoker.perform_command(AddCommand(number, 1))
        self.assertEqual(2, number.get_number())

        invoker.perform_command(SubtractCommand(number, 4))
        self.assertEqual(-2, number.get_number())

        self.assertEqual(2, len(invoker.command_history_stack))

        invoker.perform_command(MultiplyCommand(number, -2))
        self.assertEqual(4, number.get_number())

        invoker.perform_command(DivideCommand(number, 2))
        self.assertEqual(2, number.get_number())

        invoker.perform_command(AddAndMultiplyCommand(number, 7, 2))
        self.assertEqual(18, number.get_number())

        invoker.rollback_all_commands()
        self.assertEqual(1, number.get_number())


if __name__ == '__main__':
    unittest.main()
