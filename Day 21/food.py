from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.refresh()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
