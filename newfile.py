Full Source Code

Import turtle as t

import randon as d

1.bgcolor(yellow)

caterpillar turtle() caterpillar.shape('square')

caterpillar,color("red

caterpillar.speed(0)

")

caterpillar.penup() caterpillar, hideturtle()

leaf 1.Turtle()

leaf shape ((0,0),(14,2), (18,0), (20,20), (6,18),(2,14))

t.register shape("leaf, leaf shape)

leaf.shape('leaf') leaf.color('green')

leaf.penup() leaf.hideturtle()

leaf.speed()

gane started False

text turtle t.Turtle() text_turtle.write('Press SPACE to

start, align='center', font('Arial', 16, 'bold'))

text_turtle.hideturtle()

score turtlet.Turtle() score turtle.hideturtle()

score turtle.speed(0)

def outside window():

left wallt.window.width()/2

right wallt.window width()/2

top wall t.window height()/ botton wallt.window height()/2 (x,y) caterpillar.pos() outside x left wall or x right wall or y bottom wall

or y > top_wall

return outside
def game_over():

caterpillar.color('yellow') leaf.color('yellow')

t.penup()

t.hideturtle()

t.write('GAME OVER!', align='center',

font=('Aerial', 30, 'normal'))

def display_score (current_score):

score_turtle.clear() score_turtle.penup()

x = (t.window_width()/2)-50

score_turtle.setpos(x,y)

y = (t.window_height() / 2)-50 score_turtle.write(str(current_score), align= 'right', font=('Arial', 40, 'bold'))

def place leaf(): leaf.hideturtle()

leaf.setx(rd.randint(-200,200)) leaf.sety(rd.randint(-200,200))

leaf.showturtle()

def start_game():

global game_started

if game_started:

return

game_started = True

Score = 0

text_turtle.clear()

caterpillar_speed = 2

caterpillar_length # 3 caterpillar.shapesize(1, caterpillar_length,1)

caterpillar.showturtle() display_score (score)

place_leaf()

while True:

caterpillar.forward (caterpillar_speed) if caterpillar.distance(leaf)<20:
	place leaf ()

caterpillar length caterpillar_length + 1 caterpillar.shapesize(1, caterpillar_length,1) caterpillar speed caterpillar_speed + 1

score score + 10

display score(score) If outside window():

gane over( )

break

def move up():

if caterpillar.heading() == or caterpillar.heading() == 189: caterpillar.setheading (90)

def move down():

if caterpillar.heading()e or caterpillar.heading() 180: caterpillar.setheading (270)

def move_left():

If caterpillar.heading() 90 or caterpillar.heading()

270:

caterpillar.setheading(180)

def nove right():

if caterpillar.heading() 90 or caterpillar.heading() 270:

caterpillar.setheading(e)

t.onkey(start game, 'space')

t.onkey (move up, 'Up')

t.onkey(move right, "Right') t.onkey (move_down, 'Down')

t.onkey(nave left, 'Left')

t.listen()

t.mainloop()