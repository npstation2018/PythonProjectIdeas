import turtle

scr = turtle.Screen()
scr.title("Fidget Spinner!")
scr.setup(800,600,100,0)
scr.bgcolor("light blue")
t = turtle.Turtle()
t1 = turtle.Turtle()
t.hideturtle()
t1.hideturtle()
t1.penup()
t1.goto(-200,200)
t1.write("FIDGET SPINNER!!!", font = ("jokerman", 40, "bold"))
t.goto(0,-50)
t.pendown()
t.width(40)

state = {'turn':0}

def spinner():
    t.clear()
    angle = state['turn']
    t.right(angle)
    col = ['pink', 'darkseagreen1', 'gold1']
    for i in range(3):
        t.forward(160)
        t.dot(180,col[i])
        t.backward(160)
        t.right(120)
    turtle.update()
    
def animate():
    if state['turn']>0:
        state['turn']-=1
    spinner()
    turtle.ontimer(animate,10)
    
def flick():
    state['turn']+=20
    
turtle.tracer(False)
turtle.onkey(flick, 'space')
turtle.listen()
animate()
        
turtle.done()