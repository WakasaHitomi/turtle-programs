import random
from turtle import *

Wakasa = Turtle()
Momo = Turtle()
Kassie = Turtle()

Wakasa.shape("turtle")
Wakasa.color("purple")
Wakasa.shapesize(5)
Wakasa.pensize(6)
Wakasa.speed(10)


Momo.shape("turtle")
Momo.color("blue")
Momo.shapesize(5)
Momo.pensize(10)

Kassie.shape("turtle")
Kassie.color("black")
Kassie.shapesize(5)
Kassie.pensize(8)

for i in range(25):
    while True:
        Kassie.fd(200)
        Kassie.rt(30)
        Momo.lt(80)
        Wakasa.lt(5)
        Wakasa.fd(20)
        Momo.fd(180)
        Kassie.fd(90)
