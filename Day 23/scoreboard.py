from turtle import Turtle
from time import sleep

FONT = ("Courier", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("black")
        self.setpos(x=-250, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.setpos(-100, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
