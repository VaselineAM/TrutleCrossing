from turtle import Turtle
import random
colours = ["red","green","yellow","orange","black"]
import random
class rangeen(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color(random.choice(colours))
        self.shape("square")
        self.shapesize(stretch_len=1.5)
        self.goto(random.randint(100,8000),random.randint(-160,160))
    
    
