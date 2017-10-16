import random
from turtle import *

# tkinter colors

Wakasa = Turtle()
Momo = Turtle()
Kassie = Turtle()
Peter = Turtle()
Lambert = Turtle()

Wakasa.shape("turtle")
Wakasa.color("DarkOrchid1")
Wakasa.shapesize(5)
Wakasa.pensize(6)
Wakasa.speed(10)

Momo.shape("turtle")
Momo.color("turquoise")
Momo.shapesize(5)
Momo.pensize(10)
Momo.speed(10)

Kassie.shape("turtle")
Kassie.color("slate gray")
Kassie.shapesize(5)
Kassie.pensize(8)
Kassie.speed(10)

Peter.shape("turtle")
Peter.color("dark green")
Peter.shapesize(7)
Peter.pensize(3)
Peter.speed(10)

Lambert.shape("turtle")
Lambert.color("blue4")
Lambert.shapesize(1)
Lambert.pensize(10)
Lambert.speed(10)


for i in range(25):
    while True:
        Kassie.fd(50)
        Kassie.rt(50)
        Momo.lt(80)
        Wakasa.lt(10)
        Wakasa.fd(40)
        Momo.fd(180)
        Peter.fd(90)
        Peter.lt(70)
        Lambert.lt(90)
        Peter.fd(60)
        Lambert.fd(80)
        if abs(pos()) < 1:
            break
    




