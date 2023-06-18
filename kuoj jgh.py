import square

from itertools import box
colors = square(['red','orange','yellow','green','blue','purple'])

def draw_square(size,angle,shift):
    turtle.bgcolor('blue')
    turtle.pencolor(next(colors))
    turtle.square(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_square(size+5,angle+1,shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_square(30,0,1)



