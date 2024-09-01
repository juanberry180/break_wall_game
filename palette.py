from turtle import Turtle


class Palette(Turtle):
    def __init__(self, y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('black')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(0,y)


    def go_here(self,x,y):
            self.goto(x, y)









