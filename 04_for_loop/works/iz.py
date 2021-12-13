import turtle

def sneg1():
    t = turtle
    y = 0
    c = 0

    t.speed(3)
    t.pensize(5)
    t.lt(90)
    t.pu()
    t.bk(150)
    t.lt(60)
    t.fd(100)

    t.pd()
    for x in range(6):
        t.lt(180)
        t.fd(140)
        for y in range(5):
            t.rt(60)
            t.fd(40)
        t.fd(100)
        t.lt(60)

#    turtle.exitonclick()


def sneg2():
    t = turtle
    y = 0
    c = 0

    t.speed(3)
    t.pensize(5)
    t.lt(90)
    t.pu()
    t.bk(150)
    t.lt(60)
    t.fd(50)

    t.pd()
    for x in range(6):
        t.lt(180)
        t.fd(90)
        for y in range(5):
            t.rt(60)
            t.fd(40)
        t.fd(50)
        t.lt(60)

#    turtle.exitonclick()


def sneg3():
    t = turtle
    y = 0
    c = 0

    t.speed(3)
    t.pensize(5)
    t.lt(90)
    t.pu()
    t.bk(150)
    t.lt(60)
    t.fd(50)

    t.pd()
    for x in range(6):
        t.lt(180)
        t.fd(90)
        for y in range(5):
            t.rt(60)
            t.fd(40)
        t.fd(50)
        t.lt(180)

#    turtle.exitonclick()


sneg1()

turtle.left(90)
turtle.fd(100)

sneg2()

turtle.left(90)
turtle.fd(200)

sneg3()

turtle.left(90)
turtle.fd(100)

turtle.exitonclick()