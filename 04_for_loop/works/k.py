import turtle


def draw_snowflake(x, y, line=120, n=6, size=5, color='#1F75FE'):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(size)
    for _ in range(n):
        turtle.forward(line)
        turtle.backward(line / 3)
        turtle.left(45)
        turtle.forward(line / 3)
        turtle.backward(line / 3)
        turtle.right(90)
        turtle.forward(line / 3)
        turtle.backward(line / 3)
        turtle.left(45)
        turtle.backward(2 * line / 3)
        turtle.left(360 / n)


draw_snowflake(120, 100)
draw_snowflake(-120, 100, 110, size=15)
draw_snowflake(-100, -100, 90, 8)