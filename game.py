import random

class monster:
    def __init__(self, type, attack, HP):
        self.__type = type
        self.__attack = attack
        self.__HP = HP

    def take_dmg(self, attack):
        self.__HP -= attack

    def deal_dmg(self):
        return self.__attack

    def get_type(self):
        return self.__type

    def get_HP(self):
        return self.__HP

class skeleton_knight(monster):
    def __init__(self):
        super().__init__("skeleton",random.randint(8,12),15)

class slime(monster):
    def __init__(self):
        super().__init__("slime",random.randint(3,5), 25)

class Wild_boar(monster):
    def __init__(self):
        super().__init__("Wild boar",random.randint(5,9), 20)

class player:
    def __init__(self, name, monster):
        self.__name = name
        self.monster = monster

    def get_name(self):
        return self.__name

monsters = [skeleton_knight, Wild_boar, slime]

print("lets make your character!")
name = input("Choose your username ")

print("skeleton_knight # 1")
print("slime # 2")
print("wild boar # 3")

choose = True
while choose == True:
    choose = (input("what monster do you want, input its number "))
    if choose == "1":
        choosen_monster = skeleton_knight()
        choose = False
    elif choose == "2":
        choosen_monster = slime()
        Choose = False
    elif choose == "3":
        choosen_monster = Wild_boar()
        Choose = False
    else:
        print("Du måste använda dig av 1, 2 eller 3")
        choose = True
    



print(choosen_monster.get_type())
player1 = player(name, choosen_monster)
your_hp = choosen_monster.get_HP()
your_attack = choosen_monster.deal_dmg()

input(f"great {player1.get_name()}! press enter to continue ")

enemy_class = random.choice(monsters)()
enemy = enemy_class
enemy_hp = enemy.get_HP()
enemy_attack = enemy.deal_dmg()
print(f"A {enemy.get_type()} appears!")

fight = True

while fight == True:
    print(f"your {choosen_monster.get_type()} gets ready for battle ")
    print(f"your {choosen_monster.get_type()} deals {choosen_monster.deal_dmg()} dmg to the enemy monster")
    enemy_hp -= your_attack
    print(f"Enemy monster has {enemy_hp} left")

    if enemy_hp <= 0:
        print("You win!")
        fight = False

    print(f"The enemy {enemy.get_type()} attacks your monster back")
    print(f"The enemy deals{enemy_attack} to your {choosen_monster.get_type()}")
    your_hp -= enemy_attack
    print(f"your monster has {your_hp} left")

    if your_hp <= 0:
        print("You lose...")
        fight = False