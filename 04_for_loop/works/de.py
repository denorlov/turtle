import turtle
t = turtle.Turtle()
window = turtle.Screen()
t.shape("turtle")
t.pensize(3)
window.bgcolor("black")
for i in range(45):
    t.pencolor("red")
    t.forward(43)
    t.right(49)
    t.forward(43)
    t.right(58)
t.left(70)
t.forward(2)
for i in range(45):
    t.pencolor("green")
    t.forward(43)
    t.right(49)
    t.forward(43)
    t.right(58)
t.right(350)
t.forward(40)
for i in range(45):
    t.pencolor("blue")
    t.forward(43)
    t.right(49)
    t.forward(43)
    t.right(58)
turtle.exitonclick()