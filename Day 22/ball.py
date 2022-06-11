from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_movement = 10
        self.x_movement = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_movement = -self.y_movement

    def paddle_bounce(self):
        self.ball_speed *= 0.9
        self.x_movement = -self.x_movement

    def reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
