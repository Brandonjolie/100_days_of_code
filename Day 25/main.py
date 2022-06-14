import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)
data = pd.read_csv("50_states.csv")
drawer = turtle.Turtle()
drawer.hideturtle()
score = 0
tries = 0
data["state"] = data["state"]
answer_state = screen.textinput(
    title="Guess the State", prompt="What's another State's name?"
)
game_is_on = True
while game_is_on:
    tries += 1
    if len(answer_state) > 2:
        answer_state = answer_state.title()
        ans_column = data[data["state"] == answer_state]
        if len(ans_column) == 0:
            print("No state")
        else:
            ans_x = int(ans_column["x"])
            ans_y = int(ans_column["y"])
            drawer.penup()
            drawer.goto(ans_x, ans_y)
            drawer.pendown()
            drawer.write(f"{answer_state}")
            score += 1
    if tries < 50:
        answer_state = screen.textinput(
            title=f"{int(score)}/50 States Correct",
            prompt="What's another State's name?",
        )
    else:
        game_is_on = False

screen.exitonclick()
