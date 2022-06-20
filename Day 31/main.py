from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
learn_file = "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 31/data/words_to_learn.csv"
# data
try:
    data = pandas.read_csv(learn_file)
except FileNotFoundError:
    data = pandas.read_csv(
        "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 31/data/french_words.csv"
    )

dict_data = data.to_dict(orient="records")
current_word = random.choice(dict_data)

# button functions
def change_word():
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(dict_data)
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    timer = window.after(3000, flip_card)


def flip_card():
    global current_word
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    english_word = data[data["French"] == current_word["French"]]
    eng_word = english_word.to_dict(orient="records")[0]["English"]
    canvas.itemconfig(word_text, text=eng_word, fill="white")


def stop_show():
    dict_data.remove(current_word)
    df = pandas.DataFrame(dict_data)
    df.to_csv(learn_file, index=False)
    change_word()


# ui
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(
    file="//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 31/images/card_front.png"
)

card_back = PhotoImage(
    file="//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 31/images/card_back.png"
)

x_image = PhotoImage(
    file="//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 31/images/wrong.png"
)
check_image = PhotoImage(
    file="//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 31/images/right.png"
)
wrong_button = Button(image=x_image, highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=check_image, highlightthickness=0, command=stop_show)
right_button.grid(row=1, column=1)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(
    400, 150, text="French", fill="black", font=(FONT_NAME, 40, "italic")
)
word_text = canvas.create_text(
    400, 263, text=current_word["French"], fill="black", font=(FONT_NAME, 60, "bold")
)
canvas.grid(column=0, row=0, columnspan=2)
timer = window.after(3000, flip_card)
window.mainloop()
