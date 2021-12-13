import turtle

turtle.Screen().bgcolor('black')
turtle.setup(800,800)
turtle.tracer(1000,0)


r = 20
distance = 2 * r

turtle.pendown()
turtle.fillcolor('red')
turtle.color('red')
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
turtle.penup()

turtle.forward(distance)

turtle.pendown()
turtle.fillcolor('green')
turtle.color('green')
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
turtle.penup()

turtle.forward(distance)

turtle.penup()
turtle.fillcolor('blue')
turtle.color('blue')
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
turtle.forward(distance)
turtle.pendown()

turtle.exitonclick()