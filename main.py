class GameCharacter:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        raise NotImplementedError


class Warrior(GameCharacter):
    def attack(self):
        return f"⚔️ {self.name} qilich bilan {self.power} zarba berdi"


class Mage(GameCharacter):
    def attack(self):
        return f"🔥 {self.name} sehr bilan {self.power} zarar yetkazdi"


chars = [
    Warrior("Thor", 80),
    Mage("Merlin", 100)
]

for c in chars:
    print(c.attack())
