from turtle import Turtle, Screen
import turtle

screen = turtle.Screen()
turtle = Turtle()

screen.bgpic('i2gb4m7j7cb41.png')
turtle.hideturtle()

turtle.color('orange')
turtle.speed(0)

wid1 = 11
wid2 = 12
wid3 = 6

turtle.up()
turtle.circle(50, 310)
turtle.down()
turtle.width(wid1)
turtle.circle(50, 180)

turtle.up()
turtle.circle(50, 50)
turtle.down()
turtle.width(wid1)
turtle.circle(50, 80)

turtle.up()
turtle.right(90)
turtle.forward(15)
turtle.left(90)

turtle.width(wid2)
turtle.circle(65, 50)
turtle.down()
turtle.circle(65, 180)
turtle.up()
turtle.circle(65, 50)
turtle.down()
turtle.circle(65, 80)

turtle.width(wid3)
turtle.up()
turtle.right(90)
turtle.forward(30)
turtle.right(-110)
turtle.forward(175)
turtle.down()

for i in range(9):
    turtle.right(-120)
    turtle.up()
    turtle.forward(300)
    turtle.down()

    turtle.right(120)
    turtle.forward(60)
    turtle.right(70)
    turtle.forward(250)
    turtle.right(168)
    turtle.forward(275)


screen = Screen()
screen.exitonclick()