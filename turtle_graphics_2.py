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
    for i in range(72):
            lt(5)
            fd(20)
    end_fill()


speed(10)

luna_moon(-400, -50, 1, "black", "azure3")
luna_moon(400, -50, 1, "black", "azure3")

def small_dots(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(100):
            lt(15)
            fd(10)
    end_fill()


speed(10)


small_dots(-420, -100, 1, "LightBlue1", "light sky blue")

def eye_pupil(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(100):
            lt(10)
            fd(15)
    end_fill()

speed(10)


eye_pupil(-370, -40, 1, "cornsilk4", "honeydew4")
eye_pupil(170, 40, 1, "cornsilk4", "honeydew4")
