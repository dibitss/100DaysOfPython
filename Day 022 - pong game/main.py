from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

PLAYER_1_XY = (350, 0)
PLAYER_2_XY = (-350, 0)

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtong")
screen.tracer(0)

right_paddle = Paddle(position=PLAYER_1_XY)
left_paddle = Paddle(position=PLAYER_2_XY)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="q", fun=left_paddle.move_up)
screen.onkeypress(key="a", fun=left_paddle.move_down)


while True:
    sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(right_paddle) < 70 and ball.xcor() > 320 or ball.distance(left_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.update_scores("left")

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.update_scores("right")
    

screen.exitonclick()