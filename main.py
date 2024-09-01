from turtle import Turtle, Screen, window_width, window_height
import turtle
from palette import Palette
from ball import Ball
from bricks import Brick
from board import GameOver, ScoreBoard
import time



def motion(event):
    if event.x >= 40 and event.x <= screen.window_width()-40:
        x, y = event.x - screen.window_width()/2, - screen.window_height()/2+30
        palette.goto(x, y)
    elif event.x < 40:
        x, y = -screen.window_width()/2+40, - screen.window_height() / 2 + 30
        palette.goto(x, y)
    else:
        x, y = screen.window_width()/2-40, - screen.window_height() / 2 + 30
        palette.goto(x, y)

screen = Screen()
screen.setup(width=1000, height=600)
screen.title('Break Through Game')
screen.bgcolor('white')
screen.tracer(0)




canvas = screen.getcanvas()
canvas.bind('<Motion>', motion)


ball = Ball()
brick = Brick(screen.window_width(),screen.window_height())
score_board = ScoreBoard(screen.window_width(),screen.window_height(), len(brick.all_bricks))
palette = Palette(- screen.window_height() / 2 + 30)


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)
    for item in brick.all_bricks:
        if ball.distance(item) < 35:
            item.goto(1000,1000)
            ball.bounce()
            score_board.point_add()
            if score_board.bricks <= 0:
                ball.ball_speed = ball.ball_speed*0.9
                score_board.level_add()
                brick.all_bricks.clear()
                brick.create_bricks()




    if ball.xcor() >= screen.window_width()/2-20:
        ball.bounce_back()

    if ball.xcor() <= -screen.window_width()/2+20:
        ball.bounce_back()

    if ball.distance(palette) < 40:
        ball.bounce()

    if ball.ycor() <= -screen.window_height()/2+20:
        game_is_on = False
        board = GameOver()

    if ball.ycor() > screen.window_height()/2-20:
        ball.bounce()

    else:
        game_is_on = True

screen.update()

screen.mainloop()


