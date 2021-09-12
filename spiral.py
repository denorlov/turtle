import turtle
import colorsys

turtle.setup(700,700)
turtle.title("Spiral - PythonTurtle.Academy")
turtle.speed(0)
turtle.hideturtle()
n=200
s=2
for i in range(n):
    turtle.fd(s)
    turtle.left(119)
    s += 2

turtle.mainloop()