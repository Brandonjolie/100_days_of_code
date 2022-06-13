from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.filepath = "data.txt"
        self.score = 0
        with open(self.filepath) as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.setpos(x=0, y=260)
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT
        )

    def update(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(self.filepath, "w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()


# ukg = Scoreboard()
