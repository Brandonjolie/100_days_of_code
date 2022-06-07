import colorgram, random
import turtle

Turtle = turtle.Turtle
timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)

color_list = [
    (198, 13, 32),
    (40, 76, 189),
    (39, 217, 70),
    (229, 159, 46),
    (237, 225, 6),
    (28, 40, 155),
    (214, 76, 13),
    (197, 15, 11),
    (16, 154, 16),
    (242, 35, 165),
    (228, 18, 122),
    (70, 10, 31),
    (61, 15, 8),
    (224, 140, 208),
    (11, 97, 62),
    (53, 210, 229),
    (220, 159, 10),
    (18, 19, 44),
    (12, 227, 239),
    (238, 157, 215),
    (85, 75, 210),
    (83, 208, 157),
    (90, 233, 195),
    (64, 232, 240),
    (4, 68, 42),
]


def paintings():
    for _ in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


def left():
    timmy.penup()
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.pendown()


def right():
    timmy.penup()
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)
    timmy.forward(50)
    timmy.pendown()


def hirst():
    timmy.hideturtle()
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    timmy.pendown()
    for k in range(10):
        paintings()
        opts = [left, right]
        num = k % 2
        opts[num]()
    timmy.showturtle()


hirst()
Screen = turtle.Screen()
Screen.exitonclick()
