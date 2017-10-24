from turtle import *
setup(500, 500)
Screen()
Luna = Turtle()
showturtle()
Luna.pensize(10)

def forward():
    Luna.forward(5)

def right_key():
    Luna.right(5)

def left_key():
    Luna.left(5)

def back():
    Luna.back(5)

def pen():
    Luna.penup()

def pen_down():
    Luna.pendown()
   
onkeypress(forward, "Up")
onkeypress(right_key, "Right")
onkeypress(left_key, "Left")
onkeypress(back, "Down")
onkeypress(pen, "u")
onkeypress(pen_down, "d")



listen()
mainloop()
