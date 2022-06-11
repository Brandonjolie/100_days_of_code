from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_x) -> None:
        super().__init__(shape="square")
        self.color("white")
        self.parts = []
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(x=starting_x, y=0)

    def up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.setpos(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.setpos(self.xcor(), new_y)
