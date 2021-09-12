from turtle import Turtle, Screen

turtle = Turtle()

turtle.color("red")
turtle.forward(100)

screen = Screen()
screen.colormode(255)

R = 255
G = 255
B = 0

screen.bgcolor((R, G, B))

screen.exitonclick()