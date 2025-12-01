from abc import ABC, abstractmethod
import random
import time

class Action(ABC):
    @abstractmethod
    def execution(self, attaker, target):
        pass

class CriticalHit(Action):
    def execution(self, attaker, target):
        spcost = 5
        if attaker.SP >= spcost:
            attaker.SP -= spcost
            base_damage = int(attaker.ATK * 1.5)
            real_damage = max(0, base_damage - target.DEF)
            target.HP -= real_damage
            return(True, real_damage, "[Critical Hit]")
        return(False, 0, "[Critical Hit]")

class PiercingShot(Action):
    def execution(self, attaker, target):
        spcost = 10
        if attaker.SP >= spcost:
            attaker.SP -= spcost
            base_damage = 20
            real_damage = max(0, base_damage - target.DEF)
            target.HP -= real_damage
            return(True, real_damage, "[Piercing Shot]")
        return(False, 0, "[Piercing Shot]")

class FireballSpell(Action):
    def execution(self, attaker, target):
        spcost = 15
        if attaker.SP >= spcost:
            attaker.SP -= spcost
            base_damage = 40
            real_damage = max(0, base_damage - target.DEF)
            target.HP -= real_damage
            return (True, real_damage, "Fireball")
        return (False, 0, "Fireball")

class PunchKing(Action):
    def execution(self, attaker, target):
        spcost = 10
        if attaker.SP >= spcost:
            attaker.SP -= spcost
            base_damage = 25
            real_damage = max(0, base_damage - target.DEF)
            target.HP -= real_damage
            return (True, real_damage, "The King Punch")
        return (False, 0, "The King Punch")
        
class NoSpecial(Action):
    def execution(self, attaker, target):
        return (False, 0, "None")
    
class AtributosGerais(ABC):
    def __init__(self, name, HP: int, ATK: int, DEF: int, SP: int, SAction: Action):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SP = SP
        self.SAction = SAction

    def __str__(self):
            return f"|Name: {self.name}| Damage: {self.ATK}| Life: {self.HP}| Armor: {self.DEF}| Mana: {self.SP}"

#Units Creation

class Archer(AtributosGerais): pass
class Warrior(AtributosGerais): pass
class Sorcerer(AtributosGerais): pass
class GoblinKing(AtributosGerais): pass
class Goblin(AtributosGerais): pass
class Hobgoblin(AtributosGerais): pass

class UnitsType(ABC):
    
    @abstractmethod
    def Warrior_unit(self, name): pass
    @abstractmethod
    def Archer_unit(self, name): pass
    @abstractmethod
    def Sorcerer_unit(self, name): pass

class Heroes(UnitsType):

    def Warrior_unit(self, name):
        return Warrior(name, 30, 15, 10, 50, SAction = CriticalHit())

    def Archer_unit(self, name):
        return Archer(name, 20, 10, 10, 50, SAction = PiercingShot())
    
    def Sorcerer_unit(self, name):
        return Sorcerer(name, 20, 30, 10, 80, SAction = FireballSpell())

class Villains(UnitsType):

    def Warrior_unit(self, name):
        return Hobgoblin(name, 25, 15, 10, 0, SAction = NoSpecial())
    
    def Archer_unit(self, name):
        return Goblin(name, 20, 15, 5, 0, SAction = NoSpecial())
    
    def Sorcerer_unit(self, name):
        return GoblinKing(name, 80, 15, 10, 80, SAction = PunchKing())

heroes = Heroes()
villains = Villains()

HeroesList = [
    heroes.Archer_unit('Roberto Carlos'),
    heroes.Warrior_unit('Lupin'),
    heroes.Warrior_unit('Ezequiel'),
    heroes.Sorcerer_unit('Gandalf'),
]
    
VillainList = [
    villains.Sorcerer_unit("Goblin King"),
    villains.Archer_unit("Minion1"),
    villains.Warrior_unit("Hobgoblin1"),
]

#Execution

Number_List = ['1', '2']
def RandomChoice():
    return random.choice(Number_List)

def TurnAction(attaker, target):

    print(f'Soldier: {attaker.name} (HP: {attaker.HP}, SP: {attaker.SP})')
    time.sleep(1.5)
    
    #Detalhar
    move_choice = random.choices(['basic', 'special'], weights=[70, 30], k=1)[0]
    
    special_active = False
    special_damage = 0
    Attak_name = ""
    
    if move_choice == 'special':
        
        special_active, special_damage, Attak_name = attaker.SAction.execution(attaker, target)

    if special_active:
        print(f'{attaker.name} use {Attak_name}!')
        time.sleep(1.5)
        print(f'{target.name} lost {special_damage} HP (special attack)!')
        
    else: 
        if move_choice == 'special' and Attak_name != "No special":
           
            print(f'{attaker.name} try use {Attak_name}, but fail! ')
            time.sleep(1.5)
        
        print(f'{attaker.name} use basic attack!')
        time.sleep(1.5)
        
        base_damage = attaker.ATK
        real_damage = max(0, base_damage - target.DEF)
        target.HP -= real_damage
        
        print(f'{target.name} lost {real_damage} HP!')

    time.sleep(1.5)
    if target.HP < 0:
        target.HP = 0
    
    print(f'{target.name} have {target.HP} HP now!')
    time.sleep(1.5)
    
    if target.HP <= 0:
        if target in HeroesList:
            HeroesList.remove(target)
            print(f'{target.name} be defeat!')
        elif target in VillainList:
            VillainList.remove(target)
            print(f'{target.name} be defeat!')
    else:
        print(f'{target.name} still alive!')
    
    time.sleep(1.5)

def All_system(Red, Blue, random_number):

    print("The hero go ahead!")
    time.sleep(1.5)
    print(f'Heroe: {Red.name} | ATK: {Red.ATK} | HP: {Red.HP} | DEF: {Red.DEF} | SP: {Red.SP}')
    time.sleep(1.5)
    print("The villain appeared!")
    time.sleep(1.5)
    print(f'Villain: {Blue.name} | ATK: {Blue.ATK} | HP: {Blue.HP} | DEF: {Blue.DEF} | SP: {Blue.SP}')
    time.sleep(1.5)

    if random_number == '1':
          print(f'{Red.name} attack first!')
          time.sleep(1.5)
          TurnAction(Red, Blue)
          
          if Blue.HP > 0:
            print(f'\nIt is time to {Blue.name} attack back!')
            TurnAction(Blue, Red)

    else:
        print(f'{Blue.name} attack first!')
        time.sleep(1.5)
        TurnAction(Blue, Red)
          
        if Red.HP > 0:
            print(f'\nIt is time to {Red.name} attack back!')
            TurnAction(Red, Blue)

    print()
    print('This combat ended')
    print()

def IniciateBattle():

    while True:

        if not HeroesList:
            print("The Villains WIN!")
            break
        elif not VillainList:
            print("The Heroes WIN!")
            break

        random_choice1 = random.choice(HeroesList)
        random_choice2 = random.choice(VillainList)
        random_number = RandomChoice()

        print("Let's the turn begin!")
        print()
        time.sleep(1.5)
        All_system(random_choice1, random_choice2, random_number)
        time.sleep(1.5)
        print('This turn finished!')
        time.sleep(1.5)
        print('------------------')
        print()
        time.sleep(1.5)
        
IniciateBattle()