import random

class monster:
    def __init__(self):
        self.__type = NotImplemented
        self.__attack = NotImplemented
        self.__HP = NotImplemented

    def take_dmg(self, attack):
        self.__HP -= attack

    def deal_dmg(self):
        return self.__attack

class skeleton_knight(monster):
    def __init__(self):
        super().__init__()

        self.__type = "skeleton"
        self.__attack = random.randint(8,12)
        self.__HP = 15
class slime(monster):
    def __init__(self):
        super().__init__()

        self.__type = "slime"
        self.__attack = random.randint(3,5)
        self.__hp = 25
class Wild_boar(monster):
    def __init__(self):
        super().__init__()

        self.__type = "Wild boar"
        self.__attack = random.randint(5,9)
        self.__HP = 20