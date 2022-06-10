from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

BOUNDARY = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


board = Scoreboard()
food = Food()
snake = Snake()

screen.tracer(0)

screen.listen()


screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision
    if snake.snake_head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        board.update()

    # wall collision
    if (
        snake.snake_head.xcor() > BOUNDARY
        or snake.snake_head.xcor() < -BOUNDARY
        or snake.snake_head.ycor() > BOUNDARY
        or snake.snake_head.ycor() < -BOUNDARY
    ):
        game_is_on = False
        board.game_over()

    for body_part in snake.snakes[1:]:
        if snake.snake_head.distance(body_part) < 10:
            game_is_on = False
            board.game_over()

screen.exitonclick()
