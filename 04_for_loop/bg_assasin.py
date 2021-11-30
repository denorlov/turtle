from turtle import Turtle, Screen

import turtle

screen = turtle.Screen()
screen.bgpic('../images/froggy_forest.gif')

turtle = Turtle()

turtle.width(10)

turtle.left(120)

for _ in range(3):
    turtle.forward(85)
    turtle.left(120)
    turtle.forward(85)
    turtle.up()
    turtle.left(120)
    turtle.forward(85)
    turtle.down()


turtle.up()
turtle.right(90)
turtle.forward(126)
turtle.right(90)
turtle.forward(150)
turtle.left(180)
turtle.down()

turtle.left(60)

for _ in range(3):
    turtle.forward(220)
    turtle.up()
    turtle.forward(80)
    turtle.down()
    turtle.forward(70)

    turtle.right(120)

    turtle.forward(300)
    turtle.right(120)


screen = Screen()
screen.exitonclick()
