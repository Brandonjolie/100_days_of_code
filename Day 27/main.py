from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Button
def button_click():
    my_label["text"] = input.get()
    val = input.get()


my_button = Button(text="click Me", command=button_click)
my_button.grid(column=1, row=1)


my_button = Button(text="click Me", command=button_click)
my_button.grid(column=2, row=0)
# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
window.mainloop()
