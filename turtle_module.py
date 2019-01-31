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

