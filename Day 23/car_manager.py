from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.y_starting = 240
        self.x_starting = 280

    def move(self):
        for car in self.cars:
            if car.xcor() < -340:
                self.cars.remove(car)
            else:
                car.forward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT

    def create_car(self):
        random_y = random.randint(-self.y_starting, self.y_starting)
        t = Turtle("square")
        t.setheading(180)
        t.color(random.choice(COLORS))
        t.penup()
        t.setpos(self.x_starting, random_y)
        t.shapesize(stretch_len=2, stretch_wid=1)
        self.cars.append(t)

    def test_car(self):
        t = Turtle("square")
        t.setheading(180)
        t.color(random.choice(COLORS))
        t.penup()
        t.setpos(self.x_starting, -280)
        t.shapesize(stretch_len=2, stretch_wid=1)
        self.cars.append(t)
