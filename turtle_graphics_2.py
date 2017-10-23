from turtle import *

Luna = Turtle()
Lycra = Turtle()
Kassie = Turtle()
Wakasa = Turtle()
Saizo = Turtle()

def luna_moon(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(25):
            lt(10)
            fd(40)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

speed(10)

luna_moon(300, -200, 1, "black", "azure3")

