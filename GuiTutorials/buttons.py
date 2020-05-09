__author__ = 'AKAKPO SENYO BRIGHT'
from tkinter import *

root=Tk()
space=Entry(root,width=50)
space.pack()
space.insert(0,"Please enter your name: ")
def click():
    mylabel =Label(root,text="Hello " + space.get())
    mylabel.pack()

mybutton =Button(root,text="Enter Your Name",command=click).pack()

root.mainloop()
