import unittest
from unittest import TestCase
from structural.adapter.character import ICharacter
from structural.adapter.characters.dragon import Dragon
from structural.adapter.characters.goblin import Goblin
from structural.adapter.characters.magician import Magician
from structural.adapter.adapters.dragon_adapter import DragonAdapter
from structural.adapter.adapters.goblin_adapter import GoblinAdapter
from structural.adapter.adapters.magician_adapter import MagicianAdapter


class TestAdapterPattern(TestCase):
    def test(self):
        dragon_character = DragonAdapter(Dragon())
        self.assertTrue(isinstance(dragon_character, ICharacter))

        self.assertEqual(10, dragon_character.attack())
        self.assertEqual(12, dragon_character.flee())
        self.assertEqual(12, dragon_character.chase())

        goblin_character = GoblinAdapter(Goblin())
        self.assertTrue(isinstance(goblin_character, ICharacter))

        self.assertEqual(8, goblin_character.attack())
        self.assertEqual(5, goblin_character.flee())
        self.assertEqual(5, goblin_character.chase())

        magician_character = MagicianAdapter(Magician())
        self.assertTrue(isinstance(magician_character, ICharacter))

        self.assertEqual(10, magician_character.attack())
        self.assertEqual(30, magician_character.flee())
        self.assertEqual(20, magician_character.chase())


if __name__ == '__main__':
    unittest.main()
