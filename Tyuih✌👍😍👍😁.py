import turtle

from itertools import cycle
colors = cycle(['red','orange','yellow','blue'])

def draw_circle(size,angle,shift):
    turtle.bgcolor('white')
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.left(angle)
    turtle.left(shift)
    draw_circle(size+0.5,angle+0,shift+16)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(13,15,13)



