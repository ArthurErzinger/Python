from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at codemy.com')
root.iconbitmap(r'C:\Users\artho\OneDrive\Desktop\Python\Tkinter\i1.ico')

my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\artho\OneDrive\Desktop\Python\Tkinter\sum.png"))   
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()