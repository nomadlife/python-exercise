import turtle as t

def rectangle (horizontal, vertical, color) :
    t.pendown()
    t.pensize(5)
    t.shape('turtle')
    t.color(color)
    t.begin_fill()
    for counter	in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed(1) 
t.bgcolor('Dodger blue')

#feet
t.goto(-100,-150)
rectangle(50,20, 'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')


t.hideturtle()


