import random

class monster:
    def __init__(self):
        self._type = "unknown"
        self._attack = 0
        self._HP = 0

    def take_dmg(self, attack):
        self.__HP -= attack

    def deal_dmg(self):
        return self.__attack

    def get_type(self):
        return self.__type

class skeleton_knight(monster):
    def __init__(self):
        super().__init__()

        self._type = "skeleton"
        self._attack = random.randint(8,12)
        self._HP = 15
class slime(monster):
    def __init__(self):
        super().__init__()

        self._type = "slime"
        self._attack = random.randint(3,5)
        self._hp = 25
class Wild_boar(monster):
    def __init__(self):
        super().__init__()

        self._type = "Wild boar"
        self._attack = random.randint(5,9)
        self._HP = 20

class player:
    def __init__(self, name, monster):
        self.__name = name
        self.monster = monster

    def get_name(self):
        return self.__name

print("lets make your character!")
name = input("Choose your username ")

print("skeleton_knight # 1")
print("slime # 2")
print("wild boar # 3")

choose = int(input("what monster do you want, input its number "))
if choose == 1:
    choosen_monster = skeleton_knight()
elif choose == 2:
    choosen_monster = slime()
elif choose == 3:
    choosen_monster = Wild_boar()

player1 = player(name, choosen_monster)

input(f"great", player1.get_name(), "press enter to continue ")

random_enemy = monsterSUB.get_type(random)
print("you have an random encountre with a", )
        