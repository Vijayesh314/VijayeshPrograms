import time

def circle (s, x, y, z):
    s.fillcolor((int(x), int(y), int(z)))
    s.pendown()
    s.begin_fill()
    s.circle(50)
    s.end_fill()
    s.penup()
    time.sleep(0.5)

def triangle (s, x, y, z):
    s.fillcolor((int(x), int(y), int(z)))
    s.pendown()
    s.begin_fill()
    for i in range(3):
        s.forward(70)
        s.left(120)
    s.end_fill()
    s.penup()
    time.sleep(0.5)

def square (s, x, y, z):
    s.fillcolor((int(x), int(y), int(z)))
    s.pendown()
    s.begin_fill()
    for i in range(4):
        s.forward(50)
        s.left(90)
    s.end_fill()
    s.penup()
    time.sleep(0.5)

def pentagon (s, x, y, z):
    s.fillcolor((int(x), int(y), int(z)))
    s.pendown()
    s.begin_fill()
    for i in range(5):
        s.forward(50)
        s.left(72)
    s.end_fill()
    s.penup()
    time.sleep(0.5)

def hexagon (s, x, y, z):
    s.fillcolor((int(x), int(y), int(z)))
    s.pendown()
    s.begin_fill()
    for i in range(6):
        s.forward(50)
        s.left(60)
    s.end_fill()
    s.penup()
    time.sleep(0.5)
