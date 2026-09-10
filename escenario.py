import turtle
v= turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")
t.speed(10)

# 1er rectangulo
t.up()
t.goto(-700,100)
t.down()
t.fillcolor("sky blue")
t.begin_fill()
t.forward(1400)
t.left(90)
t.forward(300)
t.left(90)
t.forward(1400)
t.left(90)
t.forward(300)
t.end_fill()

# origen
t.up()
t.home()

# 2do rectangulo
t.goto(-700,-200)
t.down()
t.fillcolor("blue")
t.begin_fill()
t.forward(1400)
t.left(90)
t.forward(300)
t.left(90)
t.forward(1400)
t.left(90)
t.forward(300)
t.end_fill()

# origen
t.up()
t.home()

# montañas
t.goto(-700,100)
t.down()
t.fillcolor("brown")
t.begin_fill()
t.forward(300)
t.left(120)
t.forward(300)
t.left(120)
t.forward(300)
t.left(120)

t.forward(600)
t.left(120)
t.forward(300)
t.left(120)
t.forward(300)
t.left(120)

t.forward(600)
t.left(120)
t.forward(300)
t.left(120)
t.forward(300)
t.left(120)

t.forward(600)
t.left(120)
t.forward(300)
t.left(120)
t.forward(300)
t.left(120)
t.end_fill()
# origen
t.up()
t.home()

# sol
t.goto(200,240)
t.down()
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

# origen
t.up()
t.home()


# barquito
t.goto(-350,-100)
t.down()
t.fillcolor("green")
t.begin_fill()
t.forward(300)
t.left(45)
t.forward(100)
t.left(135)
t.forward(400)
t.left(114)
t.forward(83)
t.end_fill()
# origen
t.up()
t.home()

# bandera
t.goto(-210,-30)
t.down()
t.left(90)
t.fillcolor("orange")
t.begin_fill()
t.forward(110)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.end_fill()






turtle.done()
