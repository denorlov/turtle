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

    turtle.right(10)
    turtle.forward(55)

screen = Screen()
screen.exitonclick()
