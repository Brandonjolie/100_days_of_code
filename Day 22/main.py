from turtle import Screen, Turtle
from time import sleep
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

BOUNDARY = 280

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")

screen.tracer(0)
board = Scoreboard()
rightpaddle = Paddle(350)
leftpaddle = Paddle(-350)
ball = Ball()
screen.update()

screen.listen()
screen.onkeypress(rightpaddle.up, "8")
screen.onkeypress(rightpaddle.down, "5")
screen.onkeypress(leftpaddle.up, "W")
screen.onkeypress(leftpaddle.down, "S")

game_is_on = True
while game_is_on:
    sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    paddle_boundary = 320
    # paddle collision right/left
    if (
        ball.distance(rightpaddle) < 50
        and ball.xcor() > paddle_boundary
        or ball.distance(leftpaddle) < 50
        and ball.xcor() < -paddle_boundary
    ):
        ball.paddle_bounce()

    # left point/right point
    horizontal_boundary = 380
    if ball.xcor() > horizontal_boundary:
        ball.reset()
        board.update_score(2)

    if ball.xcor() < -horizontal_boundary:
        ball.reset()
        board.update_score(1)


screen.exitonclick()
