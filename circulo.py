import turtle
import math

v= turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")

x= int(input("x: "))
y= int(input("y: "))
r= int(input("r: "))
A= math.pi*r**2

t.up()
t.goto(x,y)
t.down()
t.pencolor("red")
t.circle(r)
print("el area del circulo es: ",A)



turtle.done()
