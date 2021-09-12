from turtle import Turtle, Screen

turtle = Turtle()

turtle.width(100)
turtle.color("green")

turtle.left(90)
turtle.circle(75, 180)
turtle.left(180)
turtle.circle(75, 180)

turtle.width(10)
turtle.color("blue")

turtle.up()
turtle.left(90)
turtle.forward(400)
turtle.down()

turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

turtle.color("black")
turtle.end_fill()

screen = Screen()
screen.exitonclick()