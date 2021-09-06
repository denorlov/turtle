import turtle

screen = turtle.Screen()
screen.setup(500, 800)
screen.tracer(0, 0)
screen.title('Wundt Illusion - PythonTurtle.Academy')
turtle.hideturtle()
turtle.speed(0)


def wundt():
    turtle.color('blue')
    for y in range(-380, 400, 40):
        turtle.up()
        turtle.goto(0, y)
        turtle.down()
        turtle.goto(-100, 0)
        turtle.up()
        turtle.goto(0, y)
        turtle.down()
        turtle.goto(100, 0)

    turtle.color('red')
    turtle.pensize(5)
    turtle.up()
    turtle.goto(-50, -350)
    turtle.seth(90)
    turtle.down()
    turtle.fd(700)
    turtle.up()
    turtle.goto(50, -350)
    turtle.seth(90)
    turtle.down()
    turtle.fd(700)


wundt()
screen.update()

input()