import turtle
v= turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")
t.speed(7)

# 1ra figura
t.up()
t.goto(-500,200)
t.down()
t.fillcolor("blue")
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()

#volver al inicio
t.up()
t.home()

# 2da figura
t.goto(-300,200)
t.down()
t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

#volver al inicio
t.up()
t.home()

# 3ra figura
t.goto(-100,200)
t.down()
t.fillcolor("yellow")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()

#volver al inicio
t.up()
t.home()

# 4ta figura
t.goto(220,200)
t.down()
t.fillcolor("green")
t.begin_fill()
t.circle(50)
t.end_fill()

#volver al inicio
t.up()
t.home()

# 5ta figura
t.goto(-450,0)
t.down()
t.fillcolor("yellow")
t.begin_fill()
t.left(45)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

#volver al inicio
t.up()
t.home()

# 6ta figura
t.goto(-300,0)
t.down()
t.fillcolor("blue")
t.begin_fill()
t.forward(100)
t.left(70)
t.forward(100)
t.left(110)
t.forward(100)
t.left(70)
t.forward(100)
t.end_fill()

#volver al inicio
t.up()
t.home()

# 7ma figura
t.goto(-100,0)
t.down()
t.fillcolor("green")
t.begin_fill()
t.forward(60)
t.left(70)
t.forward(100)
t.left(110)
t.forward(110)
t.left(100)
t.forward(96)
t.end_fill()

#volver al inicio
t.up()
t.home()

# 8va figura
t.goto(220,-50)
t.down()
t.fillcolor("red")
t.begin_fill()
t.circle(100,90)
t.circle(50,90)
t.circle(100,90)
t.circle(50,90)
t.end_fill()


turtle.done()
