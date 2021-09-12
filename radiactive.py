from turtle import *


def move(x, y):
    up()
    forward(x)
    left(90)
    forward(y)
    right(90)
    down()


width(5)
speed(10)

side = 400

outlinecol = "black"
fillcol = "yellow"

color(outlinecol)
move(-(side / 2), -(side / 2))

begin_fill()
# square
for i in range(4):
    forward(side)
    left(90)
color(fillcol)
end_fill()

angle = 60

move((side / 2), (side / 2))
color(outlinecol)
right(90 + angle / 2)

sector_radius = 160
sector_angle = 60

for i in range(3):
    begin_fill()
    # sector
    forward(sector_radius)
    left(90)
    circle(sector_radius, sector_angle)
    left(90)
    forward(sector_radius)
    left(180 - sector_angle)

    left(120)
    color(outlinecol)
    end_fill()

radius2 = 36

up()
forward(radius2)
left(90)
down()

color(fillcol)
begin_fill()
circle(radius2)
color(outlinecol)
end_fill()

mainloop()
