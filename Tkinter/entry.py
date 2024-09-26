from tkinter import *

root = Tk()
new = Tk()

e = Entry(root)
e.pack()

def myClick():
    myLabel = Label(root, text="Look I clicked a Button!")
    myLabel.pack()


myButton = Button(root, text="TEST", bg= '#33FF33', command=myClick)
myButton.pack()

root.mainloop()