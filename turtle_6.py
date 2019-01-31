# object

import turtle_module
from turtle_module import *

t1 = turtle_module.Turtle_new()
t2 = turtle_module.Turtle_new()
t3 = turtle_module.Turtle_new()

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
