import pgzrun
from random import randint
import tkinter
from tkinter import Tk, messagebox, simpledialog
import time

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
#Define ghost
ghost=Actor("ghost.png")
ghost.pos = (800,100)

#User chooses the number of ghosts following pac
'''num = simpledialog.askinteger("Number of Ghosts", "How many ghosts do you want on the screen?")
for i in range (num):
    #Create multiple actors of the ghost'''

def draw():
    screen.fill("black")
    #Pac appears on screen
    pac.draw()
    pellet.draw()
    ghost.draw()
    screen.draw.text("Score: " + str(score), center=(50,50), color="white",fontsize=60)

    if game_over:
        screen.fill("red")
        messagebox.showinfo("showinfo", "Final score" + str(score))

def place_pellet():
    pellet.x=randint(20, (WIDTH-20))
    pellet.y=randint(20, (HEIGHT-20))

def update():
    global score
    #Left Arrow key pressed makes pac go left
    if keyboard.left:
        pac.x=pac.x-4
    #Right Arrow key pressed makes pac go right
    elif keyboard.right:
        pac.x=pac.x+4
    #Up Arrow key pressed makes pac go up
    elif keyboard.up:
        pac.y=pac.y-4
    #Down Arrow key pressed makes pac go down
    elif keyboard.down:
        pac.y=pac.y+4

    #Move ghost right if it's left of pac
    if ghost.x < pac.x:
        ghost.x += 1  
    #Move ghost left if it's right of pac
    elif ghost.x > pac.x:
        ghost.x -= 1
    #Move ghost down if its above pac
    if ghost.y < pac.y:
        ghost.y += 1
    #Move ghost up if its below pac
    elif ghost.y > pac.y:
        ghost.y -= 1

    #Score increases by 10 when pac collides with pellet
    collected = pac.colliderect(pellet)
    death = pac.colliderect(ghost)
    if collected:
        score += 10
        place_pellet()

    if death:
        score -= 10

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 60.0)
place_pellet()
pgzrun.go()
