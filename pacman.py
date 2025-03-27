import pgzrun
from random import randint
from tkinter import Tk, messagebox

game_over = False
score = 0
#Dimensions of screen
HEIGHT = 800
WIDTH = 800

root = Tk() 
root.geometry("300x200")

#Define Pac Man
pac=Actor("pac.png")
pac.pos = (100,100)
#Define collectible
pellet=Actor("pellet.png")
pellet.pos = (200,200)

def draw():
    screen.fill("white")
    #Pac appears on screen
    pac.draw()
    pellet.draw()
    screen.draw.text("Score: " + str(score), center=(50,50), color="black",fontsize=60)

    if game_over:
        screen.fill("red")
        messagebox.showinfo("showinfo", "Final score" + str(score))

def place_pellet():
    pellet.x=randint(20, (WIDTH-20))
    pellet.y=randint(20, (HEIGHT-20))

def update():
    global score
    if game_over:
        return
    #Left Arrow key pressed makes pac go left
    if keyboard.left:
        pac.x=pac.x-2
    #Right Arrow key pressed makes pac go right
    elif keyboard.right:
        pac.x=pac.x+2
    #Up Arrow key pressed makes pac go up
    elif keyboard.up:
        pac.y=pac.y-2
    #Down Arrow key pressed makes pac go down
    elif keyboard.down:
        pac.y=pac.y+2
    collected = pac.colliderect(pellet)
    if collected:
        score += 10
        place_pellet()

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 60.0)
place_pellet()
pgzrun.go()
