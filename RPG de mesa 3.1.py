from abc import ABC, abstractmethod
import random
import time

Number_List = ['1', '2']
def RandomChoice():
    return random.choice(Number_List)


class AtributosGerais():
    def __init__(self, name, HP: int, ATK: int, DEF: int, SP: int):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SP = SP

    
    @abstractmethod
    def stack(self):
        
        pass

    def __str__(self):
            return f"|Name: {self.name}| Damage: {self.ATK}| Life: {self.HP}| Armor: {self.DEF}| Mana: {self.SP}"

#Heroes  
class Archer(AtributosGerais):
    def __init__(self,name, HP, ATK, DEF, SP):
        super().__init__(name, HP, ATK, DEF, SP)

    def stack(self):
        # [Piercing Shot] 
        cost_sp = 10
        if self.SP >= cost_sp:
            self.SP -= cost_sp
            damage = 20
            return (damage, cost_sp, "Piercing Shot")
        else:
            return (0, 0, "SP insufficient")

class Warrior(AtributosGerais):
    def __init__(self,name, HP, ATK, DEF, SP):
        
        super().__init__(name, HP, ATK, DEF, SP)

    def stack(self):
        # [Critical Hit]
        cost_sp = 5
        if self.SP >= cost_sp:
            self.SP -= cost_sp
            damage = int(self.ATK * 1.5)
            return (damage, cost_sp, "[Critical Hit]")
        else:
            return (0, 0, "SP insufficient")

class Sorcerer(AtributosGerais):
    def __init__(self,name, HP, ATK, DEF, SP):
       
        super().__init__(name, HP, ATK, DEF, SP)

    def stack(self):
        # [Fireball] 
        cost_sp = 15
        if self.SP >= cost_sp:
            self.SP -= cost_sp
            damage = 40
            return (damage, cost_sp, "Fireball")
        else:
            return (0, 0, "SP insufficient")

HeroesList = [
    Archer('Roberto Carlos', 20, 10, 15, 10),
    Warrior('Lupin', 30, 15, 20, 5),
    Warrior('Ezequiel', 30, 10, 25, 5),
    Sorcerer('Gandalf', 20, 30, 10, 30),
]


#Villains
class Goblinking(AtributosGerais):
    def __init__(self,name, HP, ATK, DEF, SP):
        
        super().__init__(name, HP, ATK, DEF, SP)

    def stack(self):
        # [´Punch of King] 
        cost_sp = 10
        if self.SP >= cost_sp:
            self.SP -= cost_sp
            damage = 25
            return (damage, cost_sp, "Punch of King")
        else:
            return (0, 0, "SP insufficient")
    
class Goblin(AtributosGerais):
    def __init__(self,name, HP, ATK, DEF, SP):
        
        super().__init__(name, HP, ATK, DEF, SP)

    def stack(self):
        
        return (0, 0, "No special")
    
class Hobgoblin(AtributosGerais):
    def __init__(self,name, HP, ATK, DEF, SP):
       
        super().__init__(name, HP, ATK, DEF, SP)

    def stack(self):
       
        return (0, 0, "No special")
    
VillainList = [
    Goblinking("Goblin King", 80, 15, 10, 80),
    Goblin("Minion1", 20, 15, 5, 0),
    Hobgoblin("Hobgoblin1", 25, 15, 10, 0),
]


#[------Execution------]


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
          
          move_choice = random.choice(['basic', 'special', 'basic'])
          
          special_damage, cost_sp, attack_name = (0, 0, "")
          
          if move_choice == 'special':
              
              special_damage, cost_sp, attack_name = Red.stack()


          if cost_sp > 0:
              print(f'{Red.name} use {attack_name}!')
              time.sleep(1.5)
              print(f'💥 ✨ 👹')
              time.sleep(1.5)
              received_damage = special_damage 
              Blue.HP -= received_damage
              print(f'{Blue.name} lost {received_damage} HP (damage special)!')
          
          else: 
              if move_choice == 'special':
                  print(f'{Red.name} try to use {attack_name}, but fail (SP insufficient)!')
                  time.sleep(1.5)
              
              print(f'{Red.name} use a basic attack!')
              time.sleep(1.5)
              print(f'😠 ⚔️ 👹')
              time.sleep(1.5)
              received_damage = abs(int(Red.ATK) - int(Blue.DEF))
              Blue.HP -= received_damage
              print(f'{Blue.name} lost {received_damage} HP!')

          time.sleep(1.5)
          if Blue.HP < 0:
              Blue.HP = 0
          
          print(f'{Blue.name} have {Blue.HP} HP now!')
          time.sleep(1.5)
          
          if Blue.HP <= 0:
              VillainList.remove(Blue)
              print(f'{Blue.name} is defeat!')
              time.sleep(1.5)
          else:
              print('The villain still alive!')
              time.sleep(1.5)
              
    else: 
          print(f'{Blue.name} attack first!')
          time.sleep(1.5)

          
          move_choice = random.choice(['basic', 'special', 'basic'])
          
          special_damage, cost_sp, attack_name = (0, 0, "")
          
          if move_choice == 'special':
              
              special_damage, cost_sp, attack_name = Blue.stack()
          
          if cost_sp > 0: 
              print(f'{Blue.name} use {attack_name}!')
              time.sleep(1.5)
              print(f'👹 ✨ 💥')
              time.sleep(1.5)
              received_damage = special_damage
              Red.HP -= received_damage
              print(f'{Red.name} lost {received_damage} HP (damage special)!')
              
          else: 
              if move_choice == 'special':
                  print(f'{Blue.name} try to use special, but fail (SP insufficient)!')
                  time.sleep(1.5)
                  
              print(f'{Blue.name} use a basic attack!')
              time.sleep(1.5)
              print(f'👹 ⚔️ 😱')
              time.sleep(1.5)
              received_damage = abs(int(Blue.ATK) - int(Red.DEF))
              Red.HP -= received_damage
              print(f'{Red.name} lost {received_damage} HP!')

          time.sleep(1.5)
          if Red.HP < 0:
              Red.HP = 0
              
          print(f'{Red.name} have {Red.HP} HP now!')
          time.sleep(1.5)

          if Red.HP <= 0:
              HeroesList.remove(Red)
              print(f'{Red.name} is defeat!')
              time.sleep(1.5)
          else:
              print('The heroe still alive!')
              time.sleep(1.5)   
       

#Principal function
def IniciateBattle():

    while True:

        if not HeroesList:
            print("The Villains WIN!")
            break
        elif not VillainList:
            print("The Heroes WIN!")
            break

        #Random choice of hero, villain and order of attacks
        random_choice1 = random.choice(HeroesList)
        random_choice2 = random.choice(VillainList)
        random_number = RandomChoice()

        print("Let's the games begin!")
        print()
        time.sleep(1.5)
        All_system(random_choice1, random_choice2, random_number)
        time.sleep(1.5)
        print('This turn finished!')
        time.sleep(1.5)
        print()
        print('------------------')
        print('A new turn begin!')
        print('------------------')
        print()
        time.sleep(1.5)
        
        
        
#Start the code
IniciateBattle()