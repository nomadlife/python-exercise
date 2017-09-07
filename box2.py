import turtle as t

def box(pos_x,pos_y,x,y,color):
	t.penup()
	t.goto(pos_x - x/2,pos_y - y/2)
	t.pendown()
	t.speed('normal')
	t.color(color)
	t.begin_fill()
	t.fd(x)
	t.left(90)
	t.fd(y)
	t.left(90)
	t.fd(x)
	t.left(90)
	t.fd(y)
	t.left(90)
	t.end_fill()

#foot
box(-50,-150,80,50,'blue')
box( 50,-150,80,50,'blue')

#leg
box(-50,-80,20,100,'red')
box( 50,-80,20,100,'red')

#body
box(0,50,150,150,'yellow')

#arm
box(120,70,80,20,'green')
box(-120,70,80,20,'green')

#head
box(0,160,80,70,'pink')

#eye
box(10,170,10,10,'black')
box(-10,170,10,10,'black')

#mouth
box(0,150,30,10,'black')

t.hideturtle()
input("")

