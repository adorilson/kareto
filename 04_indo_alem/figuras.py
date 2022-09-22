
import turtle
turtle = turtle.Turtle()

def line():
    turtle.forward(100)

def square(width):
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)

def triangle():
    for _ in range(3):
        turtle.forward(50)
        turtle.right(120)


def rectangle():
    for _ in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

def star():
    for _ in range(6):
        turtle.forward(50)
        turtle.right(150)
        turtle.forward(50)
        turtle.left(90)

def circle():
    turtle.circle(50)

def va_para(x, y):
    #turtle.penup()
    turtle.goto(x, y)
    #turtle.pendown()

"""
va_para(-150, 50)
star()

va_para(-50, 100)
rectangle()

va_para(50, 50)
square()

va_para(150, 50)
line()

va_para(350, 0)
circle()
"""


def goto_and_write(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    square()


start = None


def goto_and_square(x, y):
    global start
    if start is None:
        start = x, y
    else:
        width = x - start[0]

        turtle.penup()
        turtle.goto(start[0], start[1])
        turtle.pendown()

        square(width)

        start = None


def tap(x, y):
    global start
    if start is None:
        start = x, y
    else:
        end = x, y

        shape(start, end)

        start = None

def square(start, end):
    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    width = end[0] - start[0]
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)

shape = square

from turtle import onscreenclick, mainloop
onscreenclick(tap)
mainloop()


def star5():
    for _ in range(5):
        turtle.forward(50)
        turtle.right(144)


#star5()
#input()
