from tkinter import *

root = Tk()

# Creating a Label widget

mylabel = Label(root, text="Hello World!")
mylabel2= Label(root, text="My Name Is John elder")
# Shoving it onto the screen

mylabel.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)


root.mainloop()