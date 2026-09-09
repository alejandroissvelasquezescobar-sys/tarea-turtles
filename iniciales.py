import turtle
v= turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")
v.bgcolor("yellow")
t.pencolor("red")
t.pensize(30)


#1ra linea
t.up()
t.goto(-500,-300)
t.down()
t.left(90)
t.forward(500)

#volver al inicio
t.up()
t.home()

#2da linea
t.goto(-100,-300)
t.left(129)
t.down()
t.forward(640)

#volver al inicio
t.up()
t.home()

#3ra linea
t.goto(-100,-300)
t.left(90)
t.down()
t.forward(500)

#volver al inicio
t.up()
t.home()

#4ta linea
t.goto(50,-300)
t.left(90)
t.down()
t.forward(500)

#volver al inicio
t.up()
t.home()

#5ta lineal
t.goto(50,-300)
t.down()
t.forward(300)

turtle.done()
