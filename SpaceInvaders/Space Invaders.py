import turtle, random, math, winsound

from player import Player
from enemy import Enemy
from bullet import Bullet
from score import Score

# setting my screen
scr = turtle.Screen()
scr.setup(1000, 600, 0, 0)
scr.bgcolor("black")
scr.title("Space Invader Game")
scr.bgpic("space invader\dp.gif")

p = Player()
enemies = []
for i in range(8):
    enemies.append(Enemy())

b = Bullet()
s = Score()

# collision between bullet and enemy
def collisionplay(a, b):
    distance = math.sqrt(abs(math.pow((a.xcor()-b.xcor()), 2) + math.pow((a.ycor()-b.ycor()), 2)))
    if distance < 20:
        return True
    else:
        return False

def collision(a, b):
    distance = math.sqrt(abs(math.pow((a.xcor()-b.xcor()), 2) + math.pow((a.ycor()-b.ycor()), 2)))
    if distance < 25:
        return True
    else:
        return False

def fireBullet():
    global selfstate
    if b.state == "Ready":
        b.state = "Fire"
        winsound.PlaySound("space invader\laser.wav", winsound.SND_ASYNC)

        x = p.xcor()
        y = p.ycor()+30
        b.goto(x,y)
        b.showturtle()

# keybindings
turtle.listen()
turtle.onkey(p.move_left, "Left")
turtle.onkey(p.move_right, "Right")
turtle.onkey(fireBullet, "space")

# main loop
while True:
    for enemy in enemies:
        # enemy movement
        x = enemy.xcor()
        x += enemy.speedamt
        enemy.setx(x)
        # movement back and down
        if enemy.xcor() > 425:
            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
            enemy.speedamt*=-1
        if enemy.xcor() < -425:
            for j in enemies:
                y = j.ycor()
                y -= 20
                j.sety(y)
            enemy.speedamt *=-1

        # check for collision, between bullet and enemy
        if collisionplay(b, enemy):
            b.hideturtle()
            b.state = "Ready"
            winsound.PlaySound("space invader\explosion.wav", winsound.SND_ASYNC)
            b.setposition(0, -400)
            x = random.randint(-300, 300)
            y = random.randint(180, 280)
            enemy.setposition(x,y)

            # score
            s.ScoreValue += 10
            s.clear()
            s.write("Score: {}".format(s.ScoreValue), align = "left", font = ("Arial", 14, "bold"))

        # collision between player and enemy
        if collision(p, enemy):
            for e in enemies:
                e.hideturtle()
            p.hideturtle()

            # score
            s.pu()
            s.goto(0, 0)
            s.pd()
            s.write("Game Over!", align = "left", font = ("Arial", 14, "bold"))
            break            

        if enemy.ycor() <= -200:
            winsound.PlaySound("space invader\gameover.wav", winsound.SND_ASYNC)
            for j in enemies:
                j.hideturtle()
            p.hideturtle()

            # score
            s.pu()
            s.goto(0, 0)
            s.pd()
            s.write("Game Over!", align = "left", font = ("Arial", 14, "bold"))
            break

    # bullet movement
    y = b.ycor()
    y += b.speedamt
    b.sety(y)

    if b.ycor() > 150:
        b.state = "Ready"
    
    if b.ycor() > 300:
        b.hideturtle()
        b.state = "Ready"