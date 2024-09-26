from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look I clicked a Button!")
    myLabel.grid(row=0, column= 1)

myButton1 = Button(root, text="astra", command=myClick)
myButton1.grid(row= 0, column= 0)



root.mainloop()