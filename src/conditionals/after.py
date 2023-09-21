class RPGCharacter:
    def __init__(self, level: int):
        self.level = level
        self.health = 100
        self.mana = 50

    def attack(self, weapon: str) -> int:
        def default():
            return 5

        attack_to_damage = {
            "sword": self.sword_attack,
            "bow": self.bow_attack,
        }

        damage_from_attack = attack_to_damage.get(weapon, default)()
        return damage_from_attack

    def sword_attack(self) -> int:
        if self.level >= 5:
            return 20
        return 10

    def bow_attack(self) -> int:
        if self.level >= 7:
            return 30
        return 15

    def heal(self) -> int:
        if self.health <= 30:
            return self.health + 20
        elif self.health <= 50:
            return self.health + 10

        return self.health

    def cast_spell(self) -> str:
        if self.mana < 20:
            return "Not enough mana"
        if self.level >= 5:
            return self.high_level_spell()
        else:
            return self.low_level_spell()

    def high_level_spell(self) -> str:
        self.mana -= 20
        return "Fireball"

    def low_level_spell(self):
        self.mana -= 10
        return "Magic Missile"
