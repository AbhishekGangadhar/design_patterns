from structural.adapter.character import ICharacter
from structural.adapter.characters.magician import Magician


class MagicianAdapter(ICharacter):
    def __init__(self, magician: Magician):
        self.magician = magician

    def attack(self) -> int:
        return self.magician.cast()

    def flee(self) -> int:
        return self.magician.vanish()

    def chase(self) -> int:
        return self.magician.run()
