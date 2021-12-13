import turtle

turtle.Screen().bgcolor('black')
turtle.Screen().setup(1000,800)
turtle.setworldcoordinates(-1200,-1000,1200,1000)

#turtle.tracer(1000,0)
turtle.speed(0)
turtle.hideturtle()

turtle.penup()
turtle.setpos(-1100, 900)

distance = 50
r = 25

for j in range(15):
    for i in range(3):
        if j % 2 == 0:
            turtle.pendown()
            turtle.fillcolor('red')
            turtle.color('red')
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()

            turtle.forward(distance)

            turtle.pendown()
            turtle.fillcolor('pale green')
            turtle.color('pale green')
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
        else:
            turtle.pendown()
            turtle.fillcolor('pale green')
            turtle.color('pale green')
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            turtle.penup()

            turtle.forward(distance)

            turtle.pendown()
            turtle.fillcolor('red')
            turtle.color('red')
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

    if j % 2 == 0:
        turtle.right(90)
        turtle.right(90)
        turtle.forward(distance // 2)
    else:
        turtle.left(90)
        turtle.forward(distance * 2)
        turtle.left(90)
        turtle.forward(distance // 2)

turtle.done()