import turtle
V= turtle.Screen()
t= turtle.Turtle()
t.shape("arrow")
t.pensize(12)

t.color("red")
t.forward(100)

t.up()
t.goto(130,30)
t.left(90)
t.down()

t.color("yellow")
t.forward(100)

t.up()
t.goto(100,160)
t.left(90)
t.down()

t.color("green")
t.forward(100)

t.up()
t.goto(-30,130)
t.left(90)
t.down()

t.color("blue")
t.forward(100)

turtle.done()
