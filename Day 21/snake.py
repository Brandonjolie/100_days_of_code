from turtle import Turtle


class Snake:
    def __init__(self) -> None:
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snakes = []
        for position in self.starting_positions:
            self.add_segment(position)
        self.snake_head = self.snakes[0]

    def move(self):
        for seg_num in range(len(self.snakes) - 1, 0, -1):
            xcoord = self.snakes[seg_num - 1].xcor()
            ycoord = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(xcoord, ycoord)

        self.snake_head.forward(20)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def add_segment(self, position):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.setpos(position)
        self.snakes.append(t)
