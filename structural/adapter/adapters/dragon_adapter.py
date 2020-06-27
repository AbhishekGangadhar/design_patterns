from structural.adapter.character import ICharacter
from structural.adapter.characters.dragon import Dragon


class DragonAdapter(ICharacter):
    def __init__(self, dragon: Dragon):
        self.dragon = dragon

    def attack(self) -> int:
        return self.dragon.flame()

    def flee(self) -> int:
        return self.dragon.fly()

    def chase(self) -> int:
        return self.dragon.fly()
