from turtle import Turtle, Screen

turtle = Turtle()

for i in range(60):
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)

    turtle.right(60)

screen = Screen()
screen.exitonclick()
