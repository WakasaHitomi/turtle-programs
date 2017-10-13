from turtle import *

def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(points):
        fd(200)
        left(turn)
    end_fill()

speed(10)

draw_star(0, 0, 36, "orange", "pink")
draw_star(-300, 40, 36, "green", "yellow")
draw_star(300, 18, 36, "black", "purple")

done()

def draw_head(x, y, line, fill):
    penup()
    goto(x, y)
    pendown()

    color(line, fill)

    begin_fill()
    for i in range(500):
        rt(30)
        fd(60)
    end_fill()

speed(10)

draw_head(0, 0, "black", "yellow")
