from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

top = 100
all_turtles = []
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.setpos(-230, top)
    all_turtles.append(new_turtle)
    top -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for current_turtle in all_turtles:
        if current_turtle.xcor() > 230:
            is_race_on = False
            winning_color = current_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        current_turtle.forward(rand_distance)


screen.exitonclick()
