from turtle import Turtle
from bricks import Brick

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.write('GAME OVER', align="center", font=('Arial', 20, 'normal'))
        self.goto(0, 0)



class ScoreBoard(Turtle):
    def __init__(self, x , y, bricks):
        super().__init__()
        self.penup()
        self.points = 0
        self.level = 0
        self.x = x
        self.y = y
        self.bricks = bricks
        self.update()
        self.hideturtle()

    def update(self):
        self.color('blue')
        self.clear()
        self.goto(-self.x / 2 + 40, self.y / 2 - 40)
        self.write(f'Level: {self.level}, Points: {self.points}, Bricks: {self.bricks}', font=('Arial', 20, 'normal'))

    def point_add(self):
        self.points += 1
        self.bricks -= 1
        self.update()

    def level_add(self):
        self.level += 1
        self.update()













