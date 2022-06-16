from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Labels
equal_label = Label(text="is equal to", font=("Arial"))
equal_label.grid(column=0, row=1)

converted_label = Label(text="0", font=("Arial"))
converted_label.grid(column=1, row=1)

km = Label(text="km", font=("Arial"))
km.grid(column=2, row=1)

miles = Label(text="miles", font=("Arial"))
miles.grid(column=2, row=0)

# Button
def button_click():
    converted_label["text"] = int(input.get()) * 1.609


Calculate = Button(text="Calculate", command=button_click)
Calculate.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)
window.mainloop()
