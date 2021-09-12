from turtle import Turtle, Screen

turtle = Turtle()

turtle.speed(10)
turtle.forward(200)
turtle.right(45)
turtle.forward(200)
turtle.right(135)
turtle.forward(200)
turtle.right(45)
turtle.forward(200)
for i in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
turtle.left(90)
turtle.forward(200)
turtle.right(45)
turtle.forward(200)
turtle.right(135)
turtle.forward(200)
turtle.right(45)
turtle.forward(200)

screen = Screen()
screen.exitonclick()