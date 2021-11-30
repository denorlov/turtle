import turtle

turtle.speed(0)
turtle.hideturtle()
n=200
s=5
for i in range(n):
    turtle.forward(s)
    turtle.left(120)
    s += 5

turtle.mainloop()