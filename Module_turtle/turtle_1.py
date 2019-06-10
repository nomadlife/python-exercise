import turtle as t

def box(pos_x,pos_y,x,y,color):
    t.penup()
    t.goto(pos_x - x/2,pos_y - y/2)  #시작점을 약간의 계산을 통해서 변경.
    t.pendown()
    t.speed('fast')
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
    
box(-50,-150,80,50,'blue')
box( 50,-150,80,50,'blue')
 
#leg
box(-50,-100,20,100,'red')
box( 50,-100,20,100,'red')

# input('')
t.exitonclick()