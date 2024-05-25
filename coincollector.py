import pgzrun
from random import randint
width = 400
height= 400

score=0

game_over=False

fox = Actor("unicorn")
fox.pos=100, 100
coin = Actor("coin")
coin.pos=200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Final Score: " + str(score), center=(50,50), color="black",fontsize=60)


    if game_over:
        screen.fill("red")
        screen.draw.text("Final Score: " + str(score), color="black", fontsize=60)

def place_coin():
    coin.x=randint(20, (width-20))
    coin.y=randint(20, (height-20))

def time_up():
    global game_over
    game_over = True

    
def update():
    global score
    if keyboard.left:
        fox.x=fox.x-2
    elif keyboard.right:
        fox.x=fox.x+2
    elif keyboard.up:
        fox.y=fox.y-2
    elif keyboard.down:
        fox.y=fox.y+2
    coin_collected=fox.colliderect(coin)

    if coin_collected:
        score+=10
        place_coin()
        
clock.schedule(time_up, 60.0)
place_coin()
pgzrun.go()
