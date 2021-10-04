from turtle import Turtle, Screen

turtle = Turtle()

#turtle.width(100)

turtle.color("green")
turtle.begin_fill()

turtle.left(90)
turtle.circle(75)
turtle.left(180)
turtle.circle(75)

turtle.up()
turtle.left(90)
turtle.forward(200)
turtle.down()

turtle.left(90)
turtle.circle(75)
turtle.left(180)
turtle.circle(75)
turtle.end_fill()

screen = Screen()
screen.exitonclick()