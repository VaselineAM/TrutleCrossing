from turtle import Turtle
class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.lt(90)
        self.goto(0,-200)

    def moveupwards(self):
        self.fd(10)
    
    def movebackwards(self):
        self.bk(10)
