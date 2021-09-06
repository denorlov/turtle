from turtle import *

def square(length):
    for i in range(4):
        forward(length)
        left(90)

def sector(radius, angle):
    forward(radius)
    left(90)
    circle(radius, angle)
    left(90)
    forward(radius)
    left(180-angle)

def move(x, y):
    up()
    forward(x)
    left(90)
    forward(y)
    right(90)
    down()

def radioactive(radius1, radius2, side, angle=60, outlinecol="black", fillcol="yellow"):
    color(outlinecol)
    move(-(side/2), -(side/2))

    begin_fill()
    square(side)
    color(fillcol)
    end_fill()
    move((side/2), (side/2))
    color(outlinecol)
    right(90 + angle/2)

    for i in range(3):
        begin_fill()
        sector(radius1,angle)
        left(120)
        color(outlinecol)
        end_fill()

    up()
    forward(radius2)
    left(90)
    down()

    color(fillcol)
    begin_fill()
    circle(radius2)
    color(outlinecol)
    end_fill()

    up()
    left(90)
    forward(radius2)
    width(1)

reset()
width(5)
speed(1)
radioactive(160, 36, 400)
mainloop()