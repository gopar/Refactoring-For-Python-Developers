class RPGCharacter:
    def __init__(self, level):
        self.level = level
        self.health = 100
        self.mana = 50

    def attack(self, weapon):
        if weapon == "sword":
            if self.level >= 5:
                return 20
            else:
                return 10
        elif weapon == "bow":
            if self.level >= 7:
                return 30
            else:
                return 15
        else:
            return 5

    def heal(self):
        if self.health <= 30:
            return self.health + 20
        elif self.health <= 50:
            return self.health + 10
        else:
            return self.health

    def cast_spell(self):
        if self.mana < 20:
            return "Not enough mana"
        elif self.mana >= 20 and self.level >= 5:
            self.mana -= 20
            return "Fireball"
        else:
            self.mana -= 10
            return "Magic Missile"
