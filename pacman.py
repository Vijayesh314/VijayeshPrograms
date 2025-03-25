import pgzrun

game_over = False
score = 0
height = 800
width = 800

pac=Actor("pac.png")
pac.pos = (100,100)

def draw():
    screen.fill("white")
    pac.draw()
    screen.draw.text("Final Score: " + str(score), center=(50,50), color="black",fontsize=60)

    if game_over:
        screen.fill("red")
        screen.draw.text("Final Score: " + str(score), color="black", fontsize=60)

def update():
    if game_over:
        return
    if keyboard.left:
        pac.x=pac.x-2
    elif keyboard.right:
        pac.x=pac.x+2
    elif keyboard.up:
        pac.y=pac.y-2
    elif keyboard.down:
        pac.y=pac.y+2

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 60.0)
pgzrun.go()
