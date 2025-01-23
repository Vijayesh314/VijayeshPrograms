#This algorithm will calculate the energy dissipated when an asteroid hits the earth
#We will be using meters because that is the standard international unit of length (except for speed)

global mass
from math import pi
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

class Asteroid:
    def __init__(self, height, diameter, speed):
        self.height = height
        self.diameter = diameter
        self.speed = speed

    def energy_calc(self):
        #First we need to calculate the mass of the asteroid
        
        #We assume the density of the asteroid to be 5 times the density of water, so 5000 kg/m^3
        density = 5000
        radius = float(self.diameter)/2
        height = float(self.height)
        volume = pi * radius**2 * height
        mass = volume * density
        x1 = len(str(int(mass))) - 1
        n1 = round(mass/10**x1)
        delay_print("We need to multiply the density (5000 kg/m^3) by the volume of the asteroid.\n")
        if n1 == 0:
            delay_print(f"So the mass of the asteroid is {mass} kilograms")
        else:
            delay_print(f"So the mass of the asteroid is {mass} kilograms.\n")

        #Now we're going to calculate the energy released in joules

        s = round(float(self.speed)) / 3600
        energyjoules = 1/2 * (s)**2 * mass
        energytnt = energyjoules/(4.2 * 10**15)
        x2 = len(str(energytnt)) - 1
        n2 = round(mass/10**x2)
        delay_print("Now we need to multiply the mass of the asteroid by the speed in meters per second.\n")
        if n2 == 0:
            delay_print(f"So the energy during the collision is {energyjoules} joules.\n")
        else:
            delay_print(f"So the energy during the collision is {energyjoules} joules.\n")
        
        rate = (radius**2 * height) / (s)
        r = len(str(rate)) - 1
        n3 = round(rate/10**r)
        delay_print(f"So the rate of the energy dissipated is {rate}")

delay_print("Welcome to the Energy Dissipation Calculator.\n")
delay_print("You will give me the dimensions (in meters) and the speed (in mph) \nAnd I will tell you the energy released during the impact and it's attack potency.\n")
delay_print("We will assume that the asteroid has a cylindrical shape.\n")

h = input("What is the height of the asteroid in meters: ")
while h.isalpha() == True:
    delay_print("You have entered an invalid input. Please give a number.\n")
    h = input("What is the height of the asteroid in meters: ")

d = input("What is the diameter of the asteroid in meters: ")
while d.isalpha() == True:
    delay_print("You have entered an invalid input. Please give a number.\n")
    d = input("What is the diameter of the asteroid in meters: ")

s = input("What is the speed of the asteroid in meters per hour: ")
while s.isalpha() == True:
    delay_print("You have entered an invalid input. Please give a number.\n")
    s = input("What is the speed of the asteroid in meters per hour: ")

a1 = Asteroid(h, d, s)
a1.energy_calc()
