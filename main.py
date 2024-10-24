class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 10 

def attack(self, other):
        if self.hp > 0:
            other.hp -= 1
            print(f"{self.name} attaque {other.name}!")
            if other.hp <= 0:
                other.hp = 0
                print(f"{other.name} est mort!")
            else:
                print(f"{other.name} a maintenant {other.hp} HP.")
        else:
            print(f"{self.name} ne peut pas attaquer car il est mort.")