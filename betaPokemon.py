#Import Things we need
import random
import time
import sys


#The code that creates a small delay between letters
def delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.025)


def SUPER_delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.12)


class Pokemon:


  def __init__(self, name, type, moves, attack, defense, health):
    self.name = name
    self.type = type
    self.moves = moves
    self.attack = attack
    self.defense = defense
    self.health = health


  def fight(self, Pokemon2):
    print("------Pokemon Battle------")


    #Print user pokemon information
    print(f"\n{self.name}")
    print("TYPE", self.type)
    print("ATTACK", self.attack)
    print("DEFENSE", self.defense)
    print("HEALTH", self.health)


    #Print computer pokemon information
    print(f"\n{Pokemon2.name}")
    print("TYPE", Pokemon2.type)
    print("ATTACK", Pokemon2.attack)
    print("DEFENSE", Pokemon2.defense)
    print("HEALTH", Pokemon2.health)




    #Type advantages and disadvantages
    version = ['Fire', 'Water', 'Grass']
    if self.type == Pokemon2.type:
      attack1="The attack did neutral damage..."
      attack2="The attack did neutral damage..."
    elif (self.type=='Fire' and Pokemon2.type=='Water') or (self.type=='Water' and Pokemon2.type=='Grass') or (self.type=='Grass' and Pokemon2.type=='Fire'):
      Pokemon2.attack*=2
      self.attack/=2
      attack1="It's not very effective..."
      attack2="It's super effective"
    elif (self.type=='Fire' and Pokemon2.type=='Grass') or (self.type=='Water' and Pokemon2.type=='Fire') or (self.type=='Grass' and Pokemon2.type=='Water'):
      Pokemon2.attack/=2
      self.attack*=2
      attack1="It's super effective"
      attack2="It's not very effective..."


    #Application should run while pokemon still have health (AKA it finishes when you die)
    while (self.health > 0) and (Pokemon2.health > 0):


      print(f"\nGo {self.name}")
      for i, x in enumerate(self.moves):
        print(f"{i+1}.", x)
      index = int(input('Pick a move: '))
      delay_print(f"\n{self.name} used {self.moves[index-1]}!\n")


      
time.sleep(1)
      SUPER_delay_print(attack1)
