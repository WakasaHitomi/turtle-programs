from turtle import *

screensize(3000, 3000)
setup(1000, 1000)
Screen()
Luna = Turtle()
showturtle()
Luna.pensize(10)
Luna.color("black")
    
bgcolor("peru")

def outer_eye(x, y, points, line, fill):
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

outer_eye(-400, -50, 1, "black", "ivory2")
outer_eye(400, -50, 1, "black", "ivory2")

def small_dots(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(30):
            lt(15)
            fd(10)
    end_fill()


speed(10)


small_dots(-420, -100, 1, "LightBlue1", "light sky blue")
small_dots(-480, -200, 1, "LightBlue1", "light sky blue")

def eye_pupil(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(50):
            lt(10)
            fd(15)
    end_fill()

speed(10)


eye_pupil(-320, 200, 1, "cornsilk4", "honeydew4")
eye_pupil(380, 90, 1, "cornsilk4", "blue4")

print("Use the arrow keys to move the turtle.")
print("")
print("The 'd' key is pen down, while the 'u' key is to lift your pen up")
print("q = black; w = red; e = blue; r = yellow; t = white")
print("press n when you are finished drawing and you want to see a classy screen.")

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

def black():
    Luna.color("black")

def blue():
    Luna.color("blue")
    
def red():
    Luna.color("red")
    
def white():
    Luna.color("white")
    
def yellow():
    Luna.color("yellow")

def finish_screen():
    clear()
          
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

   
onkeypress(forward, "Up")
onkeypress(right_key, "Right")
onkeypress(left_key, "Left")
onkeypress(back, "Down")
onkeypress(pen, "u")
onkeypress(pen_down, "d")
onkeypress(black, "q")
onkeypress(red, "w")
onkeypress(blue, "e")
onkeypress(yellow, "r")
onkeypress(white, "t")
onkeypress(finish_screen, "n")



listen()
mainloop()
