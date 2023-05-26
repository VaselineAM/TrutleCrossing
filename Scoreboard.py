from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self,level):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-320,360)
        self.pendown
        self.write(f"Level {level}",False,"center",font=('Courier', 18, "normal"))
