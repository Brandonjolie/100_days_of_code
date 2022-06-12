import time
from turtle import Screen
import random
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

board = Scoreboard()
player = Player()
cars = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.move()
    screen.update()

    if bool(random.getrandbits(1)):
        cars.create_car()

    for car in cars.cars:
        if player.distance(car) < 20:
            screen.update()
            game_is_on = False
            board.game_over()

    if player.ycor() >= 280:
        player.setup()
        board.update_score()
        cars.level_up()

screen.exitonclick()
