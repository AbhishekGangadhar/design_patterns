import unittest
from unittest import TestCase

from structural.composite.todo import Todo
from structural.composite.project import Project


class TestComposite(TestCase):
    def test(self):
        milk = Todo("Milk")
        egg = Todo("Egg")
        groceries = Project("Groceries", [milk, egg])

        maths = Todo("Maths")
        computer_science = Todo("Computer Science")
        study = Project("Study", [maths, computer_science])

        gym = Todo("Gym")

        todo = Project("Things to do", [gym, groceries, study])

        expected_html = """
            <h1>Things to do</h1>
            <ul>
                <li>Gym</li>
                <li>
                    <h1>Groceries</h1>
                    <ul>
                        <li>Milk</li>
                        <li>Egg</li>
                    </ul>
                </li>
                <li>
                    <h1>Study</h1>
                    <ul>
                        <li>Maths</li>
                        <li>Computer Science</li>
                    </ul>
                </li>
            </ul>
        """.replace(" ", "").replace("\n", "")
        self.assertEqual(expected_html, todo.get_html().replace(" ", "").replace("\n", ""))


if __name__ == '__main__':
    unittest.main()
