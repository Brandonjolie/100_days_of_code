import turtle as turtle
from turtle import Screen, Turtle
import random

timmy_the_tutle = Turtle()
timmy_the_tutle.shape("turtle")
timmy_the_tutle.color("greenyellow")
turtle.colormode(255)

colors = [
    "red",
    "blue",
    "orange",
    "green",
    "purple",
    "khaki",
    "green yellow",
    "dark red",
    "dark orchid",
]


def draw_square(turtle_obj: Turtle):
    for _ in range(4):
        turtle_obj.forward(100)
        turtle_obj.right(90)


def dashed_line(turtle_obj: Turtle):
    for _ in range(50):
        turtle_obj.forward(10)
        turtle_obj.penup()
        turtle_obj.forward(10)
        turtle_obj.pendown()


def shape_draw(turtle_obj: Turtle, number_of_sides, angle):
    for _ in range(number_of_sides):
        turtle_obj.forward(100)
        turtle_obj.right(angle)


def draw_shapes(turtle_obj: Turtle):
    sides_count = [3, 4, 5, 6, 7, 8, 9, 10]
    angles = [360 / x for x in sides_count]

    for shape in range(len(sides_count)):
        turtle_obj.color(random.choice(colors))
        shape_draw(turtle_obj, sides_count[shape], angles[shape])


def randomcolors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk(turtle_obj: Turtle):
    options = [0, 90, 180, 270]
    for _ in range(150):
        turtle_obj.speed(0)
        turtle_obj.width(10)
        turtle_obj.color(randomcolors())
        turtle_obj.setheading(random.choice(options))
        turtle_obj.forward(50)


def spirograph(turtle_obj: Turtle):
    turtle_obj.speed(0)
    for _ in range(72):
        turtle_obj.color(randomcolors())
        turtle_obj.circle(100)
        turtle_obj.left(5)


spirograph(timmy_the_tutle)
screen = Screen()
screen.exitonclick()
