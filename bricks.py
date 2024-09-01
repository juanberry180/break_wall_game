from turtle import Turtle
import random

colors = ['red', 'blue', 'green', 'yellow']

class Brick(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.all_bricks = []
        self.create_bricks()
        self.hideturtle()

    def create_bricks(self):
        start_y = self.height/4
        for color in colors:
            start_x = -self.width / 2 + 20
            max_width = self.width-20
            while max_width > 0:
                new_brick = Turtle(shape='square')
                new_brick.penup()
                new_brick.color(color)
                brick_width = random.randint(3,3)
                new_brick.shapesize(stretch_wid=1, stretch_len=brick_width)
                new_brick.goto(start_x,start_y)
                max_width -= (brick_width*20+4)
                start_x += brick_width*20+4
                self.all_bricks.append(new_brick)
            start_y += 25





