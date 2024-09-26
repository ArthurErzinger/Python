from tkinter import *
import pyautogui
import time

i = 0
j = 0

root = Tk()
root.title("INSTALOCK")


def astra():
    i = 379
    j = 655
    pyautogui.click(x=945, y=741)
    time.sleep(1)
    repetição(i, j)

def breach():
    i = 450
    j = 657
    pyautogui.click(x=945, y=741)
    time.sleep(1)
    repetição(i, j)

def brimstone():
    i = 500
    j = 652
    pyautogui.click(x=945, y=741)
    repetição(i, j)

def chamber():
    i = 555
    j = 651
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)

def cypher():
    i = 615
    j = 651
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def fade():
    i = 685
    j = 651
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)

def gekko():
    i = 737
    j = 651
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)

def harbor():
    i = 806
    j = 651
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def jett():
    i = 862
    j = 651
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)

def kayo():
    i = 915
    j = 651
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def killjoy():
    i = 977
    j = 651
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def neon():
    i = 392
    j = 710
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)

def omen():
    i = 444
    j = 707
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def phoenix():
    i = 503
    j = 711
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def raze():
    i = 558
    j = 710
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def reyna():
    i = 616
    j = 713
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def sage():
    i = 687
    j = 713
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def skye():
    i = 735
    j = 715
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def sova():
    i = 798
    j = 713
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def viper():
    i = 865
    j = 713
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  

def yoru():
    i = 916
    j = 710
    pyautogui.click(x=970, y=742)
    time.sleep(1)
    repetição(i, j)  



myButton1 = Button(root, text="ASTRA", bg= '#33FF33', command=astra, width = 10, height=2)
myButton1.grid(row= 0, column= 0)
myButton2 = Button(root, text="BREACH", bg= '#33FF33', command=breach, width = 10, height=2)
myButton2.grid(row = 0, column= 1)
myButton3 = Button(root, text="BRIMSTONE", bg= '#33FF33', command=brimstone, width = 10, height=2)
myButton3.grid(row= 0, column= 2)
myButton4 = Button(root, text="CHAMBER", bg= '#33FF33', command=chamber, width = 10, height=2)
myButton4.grid(row = 0, column= 3)
myButton5 = Button(root, text="CYPHER", bg= '#33FF33', command=cypher, width = 10, height=2)
myButton5.grid(row= 1, column= 0)
myButton6 = Button(root, text="FADE", bg= '#33FF33', command=fade, width = 10, height=2)
myButton6.grid(row = 1, column= 1)
myButton7 = Button(root, text="GEKKO", bg= '#33FF33', command=gekko, width = 10, height=2)
myButton7.grid(row= 1, column= 2)
myButton8 = Button(root, text="HARBOR", bg= '#33FF33', command=harbor, width = 10, height=2)
myButton8.grid(row = 1, column= 3)
myButton9 = Button(root, text="JETT", bg= '#33FF33', command=jett, width = 10, height=2)
myButton9.grid(row= 2, column= 0)
myButton10 = Button(root, text="KAYO", bg= '#33FF33', command=kayo, width = 10, height=2)
myButton10.grid(row = 2, column= 1)
myButton11 = Button(root, text="KILLJOY", bg= '#33FF33', command=killjoy, width = 10, height=2)
myButton11.grid(row= 2, column= 2)
myButton12 = Button(root, text="NEON", bg= '#33FF33', command=neon, width = 10, height=2)
myButton12.grid(row = 2, column= 3)
myButton13 = Button(root, text="OMEN", bg= '#33FF33', command=omen, width = 10, height=2)
myButton13.grid(row= 3, column= 0)
myButton14 = Button(root, text="PHOENIX", bg= '#33FF33', command=phoenix, width = 10, height=2)
myButton14.grid(row = 3, column= 1)
myButton15 = Button(root, text="RAZE", bg= '#33FF33', command=raze, width = 10, height=2)
myButton15.grid(row= 3, column= 2)
myButton16 = Button(root, text="REYNA", bg= '#33FF33', command=reyna, width = 10, height=2)
myButton16.grid(row = 3, column= 3)
myButton17 = Button(root, text="SAGE", bg= '#33FF33', command=sage, width = 10, height=2)
myButton17.grid(row= 4, column= 0)
myButton18 = Button(root, text="SKYE", bg= '#33FF33', command=skye, width = 10, height=2)
myButton18.grid(row = 4, column= 1)
myButton19 = Button(root, text="SOVA", bg= '#33FF33', command=sova, width = 10, height=2)
myButton19.grid(row= 4, column= 2)
myButton20 = Button(root, text="VIPER", bg= '#33FF33', command=viper, width = 10, height=2)
myButton20.grid(row = 4, column= 3)
myButton21 = Button(root, text="YORU", bg= '#33FF33', command=yoru, width = 10, height=2)
myButton21.grid(row= 5, column= 0)






























































def repetição(i, j):
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568) 
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)  
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)  
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568) 
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)  
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)  
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568) 
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)  
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)  
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568) 
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)  
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)  
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568)
    pyautogui.click(x= i, y= j)
    time.sleep(0.1)
    pyautogui.click(x=654, y=568) 

root.mainloop()