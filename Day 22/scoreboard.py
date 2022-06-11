from turtle import Turtle
from time import sleep

ALIGN = "center"
FONT = ("Arial", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        # self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.draw_starting_line()
        self.setpos(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.left_score}      {self.right_score}", align=ALIGN, font=FONT)
        self.draw_starting_line()

    def update_score(self, user):
        if user == 1:
            self.left_score += 1
        if user == 2:
            self.right_score += 1
        self.clear()
        self.setpos(x=0, y=260)
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def draw_starting_line(self):
        top = 300
        self.setheading(270)
        starting_pos = (0, top)
        self.goto(starting_pos)
        while top > -300:
            self.penup()
            self.forward(20)
            self.hideturtle()
            self.pendown()
            self.forward(20)
            top -= 40
            self.goto(0, top)
        self.penup()


# ukg = Scoreboard()
