import turtle

turtle.Screen().bgcolor('black')
turtle.Screen().setup(1000,800)
turtle.setworldcoordinates(-500,-400,500,400)

turtle.tracer(1000,0)
#turtle.speed(0)
turtle.hideturtle()

r = 3
distance = 2 * r
cols = 1000 // distance // 3
rows = 800 // distance

turtle.penup()
turtle.setpos(-500 + distance, 400 - distance)

turtle.colormode(255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

for j in range(rows):
    for i in range(cols):
        if j % 2 == 0:
            turtle.fillcolor(RED)
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()

            turtle.forward(distance)

            turtle.fillcolor(GREEN)
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()

            turtle.forward(distance)

            turtle.fillcolor(BLUE)
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()

            turtle.forward(distance)
        else:
            turtle.fillcolor(GREEN)
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()

            turtle.forward(distance)

            turtle.fillcolor(RED)
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()

            turtle.forward(distance)

            turtle.fillcolor(BLUE)
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()

            turtle.forward(distance)

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