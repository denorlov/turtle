import turtle

turtle.Screen().bgcolor('black')
turtle.Screen().setup(1000,800)
turtle.setworldcoordinates(-1200,-1000,1200,1000)

turtle.tracer(1000,0)
turtle.hideturtle()


turtle.penup()
turtle.setpos(-1100, 900)

r = 25
distance = 2 * r

for i in range(15):
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