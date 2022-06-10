from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setpos(x=0, y=260)
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)


# ukg = Scoreboard()
