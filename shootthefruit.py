import pgzrun
from random import randint
from tkinter import Tk, simpledialog
#randint only bc its saves memory in computer
apple = Actor("apple")
ch = Actor("ch")
g = Actor("g")
score=0
root = Tk()
root.withdraw
def draw():
    screen.clear()
    apple.draw()
    ch.draw()
    g.draw()

def on_mouse_down(pos):
    global score

    if apple.collidepoint(pos):
            print("Oh no! You ate me!")
            place_apple()
            score=score+1
    else:
        print("You missed!")
        print(score)
        Continue=simpledialog.askstring('Yes or No', 'Do you wish to start again? Yes or No.')
        
            
            
            
def place_apple():
    apple.x=randint(10,800)
    apple.y=randint(10,600)
    ch.x=randint(40,800)
    ch.y=randint(40,600)
    g.x=randint(70,800)
    g.y=randint(70,600)

place_apple()
pgzrun.go()
while (Continue == 'Yes'):
    score=0
    def draw():
        screen.clear()
        apple.draw()
        ch.draw()
        g.draw()

    def on_mouse_down(pos):
        global score

        if apple.collidepoint(pos):
                print("Oh no! You ate me!")
                place_apple()
                score=score+1
        else:
            print("You missed!")
            print(score)
            Continue=simpledialog.askstring('Yes or No', 'Do you wish to start again? Yes or No.')
        
            
            
            
    def place_apple():
        apple.x=randint(10,800)
        apple.y=randint(10,600)
        ch.x=randint(40,800)
        ch.y=randint(40,600)
        g.x=randint(70,800)
        g.y=randint(70,600)

    place_apple()
    pgzrun.go()
