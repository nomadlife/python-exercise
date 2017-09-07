import turtle as t

def box(x,y,color):
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
t.penup()
t.goto(-100,-150)
t.pendown()
box(80,50,'blue')

t.penup()
t.goto(0,-150)
t.pendown()
box(80,50,'blue')




input("")

