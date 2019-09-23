import turtle

t=turtle.Turtle('turtle')
t.up()
t.goto(0,-130)
t.down()
t.lt(45)
t.color('gold')
t.begin_fill()
for m in range (4):
    t.fd(320)
    t.lt(90)
t.end_fill()
t.left(45)
t.fd(15)
t.rt(45)
t.color('black')
t.pensize(4)

for i in range (4):
    t.fd(300)
    t.lt(90)

t.up()
t.goto(0,-60)
t.down()
t.setheading(90)

t.pensize(50)
t.fd(120)
t.circle(80,90)

t.up()
t.goto(0,-60)
t.down()
t.setheading(90)

t.pensize(50)
t.fd(120)
t.circle(-80,90)

t1=turtle.Turtle('arrow')
t1.shapesize(5)
t1.up()
t1.goto(70,140)
t1.stamp()

t1=turtle.Turtle('arrow')
t1.shapesize(5)
t1.up()
t1.goto(-70,140)
t1.left(180)
t1.stamp()

t2=turtle.Turtle('square')
t2.shapesize(1,2.5)
t2.color('gold')
t2.up()
t2.goto(0,-75)

