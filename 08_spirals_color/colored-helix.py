import turtle

screen = turtle.Screen()
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(1000, 10)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')

for x in range(360*2):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
    screen.update()

screen.exitonclick()