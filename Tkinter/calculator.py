from tkinter import *
from tkinter import ttk

root = Tk()
root.title("CALCULATOR")
root.geometry("460x327")

#icon photo = only .png <-----> iconbitmap = only .ico
img = PhotoImage(file= r'C:\Users\artho\OneDrive\Desktop\Python\Tkinter\images\i1.png')
root.iconphoto(False, img)
root.iconbitmap(r'C:\Users\artho\OneDrive\Desktop\Python\Tkinter\images\i1.ico')

#DISPLAY:
e = Entry(root, width=30, borderwidth=5, justify=CENTER)
e.grid(row=0, column=1, columnspan=2, pady=10)

#MENU
mb=  Menubutton ( root, text="MENU", relief=RAISED )
mb.grid(row=0, column=0)

#HISTÓRICO
iconHistory = PhotoImage(file= r'C:\Users\artho\OneDrive\Desktop\Python\Tkinter\images\history.png')

def historic():
   historic = Tk()
   historic.title(" ")
   historic.iconbitmap(r'C:\Users\artho\OneDrive\Desktop\Python\Tkinter\images\history.ico')


   historic.mainloop()

historic = []


history = Button(root, image= iconHistory, command=lambda: historic())
history.grid(row=0, column=3)

def getHistory():
   if math == "s":
      result = float(pre) + float(current)
   elif math == "sub":
      result = float(pre) - float(current)
   elif math == "pro":
      result = float(pre) * float(current)
   elif math == "div":
      result = float(pre) / float(current)
      e.insert(0, float(result))
      historic.append(str(pre) + " ÷ " + str(current) + " = " + str(result))
      print(historic)




#NUMBER BUTTONS:
button0 = Button(root, text=0, width=15, height=3, command=lambda: click(0), bg="#FFFFFF")
button1 = Button(root, text=1, width=15, height=3, command=lambda: click(1), bg="#FFFFFF")
button2 = Button(root, text=2, width=15, height=3, command=lambda: click(2), bg="#FFFFFF")
button3 = Button(root, text=3, width=15, height=3, command=lambda: click(3), bg="#FFFFFF")
button4 = Button(root, text=4, width=15, height=3, command=lambda: click(4), bg="#FFFFFF")
button5 = Button(root, text=5, width=15, height=3, command=lambda: click(5), bg="#FFFFFF")
button6 = Button(root, text=6, width=15, height=3, command=lambda: click(6), bg="#FFFFFF")
button7 = Button(root, text=7, width=15, height=3, command=lambda: click(7), bg="#FFFFFF")
button8 = Button(root, text=8, width=15, height=3, command=lambda: click(8), bg="#FFFFFF")
button9 = Button(root, text=9, width=15, height=3, command=lambda: click(9), bg="#FFFFFF")

root.bind("<Return>", button5)


#OPERATIONS:

#SOMA
def s():
    global pre
    global math
    math = "s"
    pre = float(e.get())
    e.delete(0, END)

sum = Button(root, text="+", width=15, height=3, command=lambda: s())

#SUBTRAÇÃO
def sub():
    global pre
    global math
    math = "sub"
    pre = float(e.get())
    e.delete(0, END)

subtract = Button(root, text="-", width=15, height=3, command=lambda: sub())

#MULTIPLICAÇÃO
def pro():
    global pre
    global math
    math = "pro"
    pre = float(e.get())
    e.delete(0, END)

product = Button(root, text="*", width=15, height=3, command=lambda: pro())

#DIVISÃO
def div():
    global pre
    global math
    math = "div"
    pre = float(e.get())
    e.delete(0, END)

division = Button(root, text="÷", width=15, height=3, command=lambda: div())

#IGUAL
def eq(pre):
   global current
   current = e.get()
   e.delete(0, END)

   if math == "s":
      result = float(pre) + float(current)
      spli = str(result).split(".")
      if spli[1] == "0":
         e.insert(0, int(result))
      else:
         e.insert(0, result)
   elif math == "sub":
      result = float(pre) - float(current)
      spli = str(result).split(".")
      if spli[1] == "0":
         e.insert(0, int(result))
      else:
         e.insert(0, result)
   elif math == "pro":
      result = float(pre) * float(current)
      spli = str(result).split(".")
      if spli[1] == "0":
         e.insert(0, int(result))
      else:
         e.insert(0, result)
   elif math == "div":
      result = float(pre) / float(current)
      spli = str(result).split(".")
      if spli[1] == "0":
         e.insert(0, int(result))
      else:
         e.insert(0, result)

          
equal = Button(root, text="=", width=32, height=3, command= lambda: eq(pre))


#EXTRAS:

#CLEAR
def cle():
    e.delete(0, END)

clear = Button(root, text="CLEAR", width=15, height=3, command= lambda: cle())

#BACKSPACE
def delete():
    global numLen
    numLen = len(e.get())
    e.delete(numLen - 1, END)

backspace = Button(root, text="⌫", width=15, height=3, command= lambda: delete())

#SINAL (+/-)
def sig():
   c = e.get()
   if c[0] == "-":
      e.delete(0)
   else:
       e.insert(0, "-")

signal = Button(root, text="±", width=15, height=3, command=lambda: sig())

#PONTO
def dot():
   if (str(e.get())).count(".") > 0:
      pass
   else:
      e.insert(END, ".")


ponto = Button(root, text=".", width=15, height=3, command=lambda: dot())

#CLIQUE
def click(number):
    c = e.get()
    e.delete(0, END)
    e.insert(0, str(c) + str(number))

#ROWS:

#ROW 1
sum.grid(row=1, column=0)
subtract.grid(row=1, column=1)
product.grid(row=1, column=2)
division.grid(row=1, column=3)

#ROW 2
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
clear.grid(row=2, column=3)

#ROW 3
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
signal.grid(row=3, column=3)

#ROW 4
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
backspace.grid(row=4, column=3)

#ROW 5
button0.grid(row=5, column=0)
ponto.grid(row=5, column=1)
equal.grid(row=5, column=2, columnspan=2)

root.mainloop()