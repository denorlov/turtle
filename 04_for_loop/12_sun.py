from turtle import Turtle, Screen

turtle = Turtle()

turtle.left(180+45)
turtle.forward(300)
turtle.right(180+45)

for j in range(9):
    for i in range(2):
        turtle.circle(100, 90)
        turtle.left(180)
        turtle.circle(100, -90)
        turtle.left(180)
    turtle.right(160)

screen = Screen()
screen.exitonclick()
