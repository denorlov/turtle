# see https://pythonturtle.academy/colored-slanted-fractal-tree-source-code/

import turtle

screen = turtle.Screen()
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(1000, 10)
turtle.speed(0)

def slanted_tree(x,y,length,direction):
    if length < 2: return
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(direction)
    turtle.pensize(length/50)
    turtle.color((0.5-length/L*0.5,0.5-length/L*0.5,0.5-length/L*0.5))
    turtle.fd(length)
    px,py = turtle.xcor(), turtle.ycor()
    slanted_tree(px,py,length*0.7,direction+60)
    slanted_tree(px,py,length*0.7,direction-30)

L=400
slanted_tree(100,-500,L,90)
screen.update()

screen = Screen()
screen.exitonclick()