import turtle

turtle.speed(0)
turtle.hideturtle()

n=100
s=5
for i in range(n):
    turtle.forward(s)
    turtle.left(95)
    s += 5

turtle.mainloop()