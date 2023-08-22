from tkinter import *


def button_clicked():
    print("I got clicked!")
    my_label.config(text=my_input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="Oops changed text", padx=50, pady=50)
my_label.grid(column=0, row=0)


my_button = Button(text="Click Me!", command=button_clicked)
my_button.grid(column=1, row=1)

my_input = Entry(width=10)
my_input.grid(column=3, row=2)

new_button = Button(text="New Button!")
new_button.grid(column=2, row=0)



window.mainloop()
