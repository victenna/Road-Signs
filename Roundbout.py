import turtle
t=turtle.Turtle('turtle')
t.hideturtle()
#turtle.tracer(2)
t.up()
t.color('black')
t.pensize(2)
t.goto(0,-130)
t.setheading(0)
t.down()
t.circle(130)
t.up()
t.goto(0,-120)
t.color('blue')
t.down()
t.begin_fill()
t.circle(120)
t.end_fill()

def triangle(x,y,length,angle):
    t.up()
    t.goto(x,y)
    t.down()
    t.color('white')
    t.setheading(angle)
    t.begin_fill()
    for i in range(3):


        t.fd(length)
        t.lt(120)
    t.end_fill()

t.up()
t.goto(0,-88)
t.down()
t.color('white')
t.pensize(15)
t.circle(88)

def line(angle):
    t.up()
    t.goto(0,0)
    t.setheading(angle)
    t.color('blue')
    t.pensize(85)
    t.down()
    t.fd(75)

line(10)
line(140)
line(260)

t.pensize(2)
triangle(60,-30,50,0)
triangle(-80,-80,50,0)
triangle(-50,65,50,0)
