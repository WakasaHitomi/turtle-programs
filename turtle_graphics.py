from turtle import *

Luna = Turtle()
Luna = Turtle()


def forward():
    move.forward(5)

def right_key():
    mover.right(5)

def left_key():
    move.left(5)

def back():
    move.back(5)

onkeypress(forward, "Up")
onkeypress(right_key, "Right")
onkeypress(left_key, "Left")
onkeypress(back, "Down")
