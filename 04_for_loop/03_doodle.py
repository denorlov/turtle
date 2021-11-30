from turtle import Turtle, Screen

turtle = Turtle()

for i in range(10):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

    turtle.forward(50)
    turtle.right(90)

    turtle.forward(50)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)

    turtle.forward(25)
    turtle.right(90)

    turtle.forward(25)
    turtle.right(90)

    turtle.left(45)
    turtle.forward(100)

screen = Screen()
screen.exitonclick()
