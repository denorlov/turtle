import turtle

times = 8
angel = 360 / times
steps = 100
for i in range(times):
    turtle.forward(steps)
    turtle.left(angel)

turtle.Screen().exitonclick()