from tkinter import *
from tkinter import messagebox
import random, pyperclip, json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    name = username_input.get()
    pwd = password_input.get()
    webs = website_input.get()
    new_data = {webs: {"name": name, "pwd": pwd}}

    if len(pwd) == 0 or len(name) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
        return

    try:
        with open(
            "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 30/data.json",
            "r",
        ) as open_file:
            data = json.load(open_file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data

    with open(
        "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 30/data.json", "w"
    ) as open_file:
        json.dump(data, open_file, indent=4)
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    try:
        with open(
            "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 30/data.json",
            "r",
        ) as open_file:
            data = json.load(open_file)
            webs = website_input.get()
            website = data[webs]
            messagebox.showinfo(
                title=webs,
                message=f"Email:{website['name']}\nPassword:{website['pwd']}",
            )
    except KeyError:
        messagebox.showerror(
            title="No Website",
            message="Website entered does not have a saved password",
        )
    except FileNotFoundError:
        messagebox.showerror(
            title="No Password File",
            message="Password file does not exist",
        )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=30)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky="w")

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_input = Entry(width=30)
username_input.grid(column=1, row=2, columnspan=2, sticky="w")
username_input.insert(0, "test@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=30)
password_input.grid(column=1, row=3, sticky="w")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="w")

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(
    file="//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 29/logo.png"
)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

window.mainloop()
