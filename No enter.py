import turtle
t=turtle.Turtle('turtle')
t.up()
t.color('black')
t.pensize(2)
t.goto(0,-130)
t.setheading(0)
t.down()
t.circle(130)
t.up()
t.goto(0,-120)
t.color('red')
t.down()
t.begin_fill()
t.circle(120)
t.end_fill()
t.up()
t.goto(-90,-30)
t.down()
t.color('white')
t.begin_fill()
for m in range(2):
    t.fd(180)
    t.left(90)
    t.fd(60)
    t.left(90)
t.end_fill()
t.hideturtle()
