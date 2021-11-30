from turtle import Turtle, Screen

turtle = Turtle()

for i in range(10):
    turtle.circle(100)
    turtle.right(40)

screen = Screen()
screen.exitonclick()
