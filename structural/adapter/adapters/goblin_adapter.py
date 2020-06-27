from structural.adapter.character import ICharacter
from structural.adapter.characters.goblin import Goblin


class GoblinAdapter(ICharacter):
    def __init__(self, goblin: Goblin):
        self.goblin = goblin

    def attack(self) -> int:
        return self.goblin.stab()

    def flee(self) -> int:
        return self.goblin.run()

    def chase(self) -> int:
        return self.goblin.run()
