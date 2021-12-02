import turtle

times = 100
angel = 360 / times
steps = 10
for i in range(times):
    turtle.forward(steps)
    turtle.left(angel)

screen.exitonclick()