class monster:
    def __init__(self,type,attack,HP):
        self.__type = type
        self.__attack = attack
        self.__HP = HP

    def take_dmg(self, attack):
        self.__HP -= attack

    def deal_dmg(self):
        return self.__attack
