from myturtles import *
import turtle as t
import random

num = input("1) Circle \n2) Triangle \n3) Square \n4) Pentagon \n5) Hexagon\nEnter the number of the shape you want: ")
while num.isnumeric() == False:
    print("Invalid input")
    num = input("1) Circle \n2) Triangle \n3) Square \n4) Pentagon \n5) Hexagon\nEnter the number of the shape you want: ")
shapeList = [circle, triangle, square, pentagon, hexagon]
num = int(num) - 1

def drawshape(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range (6):
        r = int(random.randrange(0,256))
        g = int(random.randrange(0,256))
        b = int(random.randrange(0,256))
        shapeList[num](t, r, g, b)
        t.penup()
        t.goto(t.xcor()+125, t.ycor())
        t.pendown()

wn = t.Screen()
wn.setup(width=800, height=800)
t.colormode(255)
t.speed(0)
if num==1:
    x = -300
else:
    x=-400

for i in range(5):
    y = 200-int(i)*125
    drawshape(x, y)

t.mainloop()
