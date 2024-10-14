import turtle as t
import time

def circle (color, s):
    s.fillcolor(color)
    s.pendown()
    s.begin_fill()
    s.circle(100)
    s.end_fill()
    s.penup()
    time.sleep(2)
    s.clearscreen()

def triangle (color, s):
    s.fillcolor(color)
    s.pendown()
    s.begin_fill()
    for i in range(3):
        s.forward(175)
        s.left(120)
    s.end_fill()
    s.penup()
    time.sleep(2)
    s.clearscreen()

def square (color, s):
    s.fillcolor(color)
    s.pendown()
    s.begin_fill()
    for i in range(4):
        s.forward(175)
        s.left(90)
    s.end_fill()
    s.penup()
    time.sleep(2)
    s.clearscreen()

def pentagon (color, s):
    s.fillcolor(color)
    s.pendown()
    s.begin_fill()
    for i in range(5):
        s.forward(175)
        s.left(72)
    s.end_fill()
    s.penup()
    time.sleep(2)
    s.clearscreen()

def hexagon (color, s):
    s.fillcolor(color)
    s.pendown()
    s.begin_fill()
    for i in range(6):
        s.forward(175)
        s.left(60)
    s.end_fill()
    s.penup()
    time.sleep(2)
    s.clearscreen()

circle("red", t)
triangle("blue", t)
square("yellow", t)
pentagon("green", t)
hexagon("blue", t)
