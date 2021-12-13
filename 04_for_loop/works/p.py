import turtle

a = 100
b = 9
turtle.color('#e6d073')
while a > 20:
    turtle.penup()
    turtle.left(90)
    turtle.pendown()
    a -= 20
    for i in range(b):
        turtle.begin_fill()
        turtle.forward(a)
        turtle.left(140)
        turtle.forward(a)
        turtle.left(-100)
        turtle.end_fill()
    turtle.left(100)
    turtle.forward(-a)
    b += 3