from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.colormode(255)

turtle.speed(0)
turtle.width(5)

R = 255
G = 1
B = 1

screen.bgcolor((255, 255, 255))

for i in range(5000):
  G += 0.5
  B += 0.5
  #R -= 1
  turtle.color((int(R % 255), int(G % 255), int(B % 255)))
  turtle.forward(i)
  turtle.right(98)