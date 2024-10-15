from myturtles import *
import turtle as t
import random

'''shape = input("What shape do you want to have drawn? Circle, Triangle, Square, Pentagon, Hexagon: ")
while shape.lower() not in ["circle", "triangle", "square", "pentagon", "hexagon"]:
    print("Invalid input")
    shape = input("What shape do you want to have drawn? Circle, Triangle, Square, Pentagon, Hexagon: ")
user = shape.lower()'''

wn = t.Screen()
wn.setup(width=900, height=900)
t.colormode(255)
t.speed(0)

for i in range (100):
    r = int(random.randrange(0,256))
    g = int(random.randrange(0,256))
    b = int(random.randrange(0,256))
    circle(t, r, g, b)
    t.penup()
    t.goto(random.randrange(-400, 400), random.randrange(-400, 400))
    t.pendown()

wn.mainloop()
