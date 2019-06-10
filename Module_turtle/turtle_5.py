# object

import turtle

class Turtle_new(turtle.Turtle):
    def box(self, pos_x, pos_y, x, y, color):
        self.penup()
        self.goto(pos_x - x/2,pos_y - y/2)  #시작점을 약간의 계산을 통해서 변경.
        self.pendown()
        self.speed('fast')
        self.color(color)
        self.begin_fill()
        self.fd(x)
        self.left(90)
        self.fd(y)
        self.left(90)
        self.fd(x)
        self.left(90)
        self.fd(y)
        self.left(90)
        self.end_fill()

t1 = Turtle_new()
t2 = Turtle_new()
t3 = Turtle_new()

t1.shape('turtle')
t1.color('red')
t1.fd(50)
t1.box(100,0,50,50,'red')

t2.shape('turtle')
t2.color('blue')
t2.left(90)
t2.fd(70)
t2.box(0,100,50,50,'blue')

t3.shape('turtle')
t3.color('green')
t3.box(-50,0,80,50,'green')

turtle.exitonclick()
# turtle.bye()

