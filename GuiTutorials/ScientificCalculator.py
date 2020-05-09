__author__ = 'AKAKPO SENYO BRIGHT'
from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.resizable(width=False,height=False)
root.configure(background="powder blue")
root.geometry("480x568+0+0")

Calculate=Frame(root)
Calculate.grid()



##########################Menu Section######################################
def Exit():
    Exit= tkinter.messagebox.askyesno("Scientific Calculator","Yes if you want to Exit")
    if Exit > 0:
        root.destroy()
        return
def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("944x568+0+0")
    return
def Standard():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")
    return
MenuBar=Menu(Calculate)
MenuList=Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="Menu", menu=MenuList)
MenuList.add_command(label="Standard",command=Standard)
MenuList.add_separator()
MenuList.add_command(label="Scientific", command=Scientific)
MenuList.add_separator()
MenuList.add_command(label="Exit", command=Exit)
########################Help Section##########################
HelpList=Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="Help", menu=HelpList)
HelpList.add_command(label="View help")

################ Main Display Section #########################################
Display=Entry(Calculate,width=30,justify=RIGHT,font=("arial",20,'bold'),bd=15,bg="powder blue")
Display.grid(row=0,column=0, columnspan=4,pady=1)
Display.insert(0,"0")

Numbers="789456123"
x=0
buttton=[]
for i in range(2,5):
    for j in range(3):
        buttton.append(Button(Calculate,width=6,height=2,font=("arial",20,'bold'),bd=4,text=Numbers[x]))
        buttton[x].grid(row=i,column=j,pady=1)
        buttton[x]["command"]= lambda a = Numbers[x]:added_value.numberInput(a)
        x+=1


########################### Function initialization #####################################
class Solve():
    def __init__(self):
        self.total=0
        self.current=""
        self.input=True
        self.sum=False
        self.operator=""
        self.result=False

    def display(self,value):
        Display.delete(0,END)
        Display.insert(0,value)

    def numberInput(self,num):
        self.result=False
        First_num=Display.get()
        Second_num=str(num)

        if self.input:
            self.current=Second_num
            self.input=False
        else:
            if Second_num==".":
                if Second_num in First_num:
                    return
            self.current= First_num + Second_num
        self.display(self.current)

    def total(self):
        self.result=True
        self.current=float(self.current)
        if self.sum == True:
            self.valid_function()
        else:
            self.total=float(Display.get())

    def valid_function(self):
        if self.operator=="add":
            self.total+=self.current
        if self.operator=="sub":
            self.total-=self.current
        if self.operator=="mul":
            self.total*= self.current
        if self.operator=="div":
            self.total/= self.current
        if self.operator=="mod":
            self.total%= self.current
        self.input=True
        self.sum=False
        self.display(self.total)

    def operate(self,operator):
        self.current=float(self.current)
        if self.sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input=True
        self.sum=True
        self.operator= operator
        self.result=False
    def Sum_total(self):
        self.result=True
        self.current = float(self.current)
        if self.sum==True:
            self.valid_function()
        else:
            self.total=float(Display.get())

    def pi(self):
        self.result=False
        self.current= math.pi
        self.display(self.current)
    def DivAdd(self):
        self.result=False
        self.current= -(float(Display.get()))
        self.display(self.current)
    def tau(self):
        self.result=False
        self.current= math.tau
        self.display(self.current)
    def e(self):
        self.result=False
        self.current= math.e
        self.display(self.current)
    def deg(self):
        self.result=False
        self.current= math.degrees(float(Display.get()))
        self.display(self.current)
    def log(self):
        self.result=False
        self.current= math.log(float(Display.get()))
        self.display(self.current)
    def log2(self):
        self.result=False
        self.current= math.log2(float(Display.get()))
        self.display(self.current)
    def log10(self):
        self.result=False
        self.current= math.log10(float(Display.get()))
        self.display(self.current)
    def log1p(self):
        self.result=False
        self.current= math.log1p(float(Display.get()))
        self.display(self.current)
    def cos(self):
        self.result=False
        self.current= math.cos(float(Display.get()))
        self.display(self.current)
    def cosh(self):
        self.result=False
        self.current= math.cosh(float(Display.get()))
        self.display(self.current)
    def acosh(self):
        self.result=False
        self.current= math.acosh(float(Display.get()))
        self.display(self.current)
    def sin(self):
        self.result=False
        self.current= math.sin(float(Display.get()))
        self.display(self.current)
    def sinh(self):
        self.result=False
        self.current= math.sinh(float(Display.get()))
        self.display(self.current)
    def asinh(self):
        self.result=False
        self.current= math.asinh(float(Display.get()))
        self.display(self.current)
    def tan(self):
        self.result=False
        self.current= math.tan(float(Display.get()))
        self.display(self.current)
    def tanh(self):
        self.result=False
        self.current= math.tanh(float(Display.get()))
        self.display(self.current)
    def atanh(self):
        self.result=False
        self.current= math.atanh(float(Display.get()))
        self.display(self.current)
    def exmp1(self):
        self.result=False
        self.current= math.expm1(float(Display.get()))
        self.display(self.current)
    def exp(self):
        self.result=False
        self.current= math.exp(float(Display.get()))
        self.display(self.current)
    def igamma(self):
        self.result=False
        self.current= math.lgamma(float(Display.get()))
        self.display(self.current)
    def Sqrt(self):
        self.result=False
        self.current= math.sqrt(float(Display.get()))
        self.display(self.current)
    def Clear(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input=True
    def ClearAll(self):
        self.Clear()
        self.total=0






added_value=Solve()
######################## Standard Section ################################################
buttton_clear=Button(Calculate,text=chr(67),width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.Clear).grid(row=1,column=0,pady=1)
buttton_clearAll=Button(Calculate,text=chr(67)+chr(69),width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.ClearAll).grid(row=1,column=1,pady=1)
buttton_SquareRoot=Button(Calculate,text="√",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.Sqrt).grid(row=1,column=2,pady=1)
buttton_Add=Button(Calculate,text="+",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= lambda :added_value.operate("add")).grid(row=1,column=3,pady=1)

buttton_Sub=Button(Calculate,text="-",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= lambda :added_value.operate("sub")).grid(row=2,column=3,pady=1)
buttton_Mul=Button(Calculate,text="×",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= lambda :added_value.operate("mul")).grid(row=3,column=3,pady=1)
buttton_Div=Button(Calculate,text="÷",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= lambda :added_value.operate("div")).grid(row=4,column=3,pady=1)

buttton_Zero=Button(Calculate,text="0",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= lambda :added_value.numberInput(0)).grid(row=5,column=0,pady=1)
buttton_Dot=Button(Calculate,text=".",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= lambda :added_value.numberInput('.')).grid(row=5,column=1,pady=1)
buttton_DivAdd=Button(Calculate,text=chr(177),width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.DivAdd).grid(row=5,column=2,pady=1)
buttton_Equal=Button(Calculate,text="=",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.Sum_total).grid(row=5,column=3,pady=1)

######################## Scientific Section ######################################################
buttton_Pi=Button(Calculate,text="∏",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.pi).grid(row=1,column=4,pady=1)
buttton_Cos=Button(Calculate,text="cos",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.cos).grid(row=1,column=5,pady=1)
buttton_Tan=Button(Calculate,text="tan",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.tan).grid(row=1,column=6,pady=1)
buttton_Sin=Button(Calculate,text="sin",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.sin).grid(row=1,column=7,pady=1)

buttton_2pi=Button(Calculate,text="2∏",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.tau).grid(row=2,column=4,pady=1)
buttton_Cosh=Button(Calculate,text="cosh",width=6,height=2,font=("arial",20,'bold'),bd=4,command= added_value.cosh).grid(row=2,column=5,pady=1)
buttton_Tanh=Button(Calculate,text="tanh",width=6,height=2,font=("arial",20,'bold'),bd=4,command= added_value.tanh).grid(row=2,column=6,pady=1)
buttton_Sinh=Button(Calculate,text="sinh",width=6,height=2,font=("arial",20,'bold'),bd=4,command= added_value.sinh).grid(row=2,column=7,pady=1)

buttton_Log=Button(Calculate,text="log",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.log).grid(row=3,column=4,pady=1)
buttton_Exp=Button(Calculate,text="Exp",width=6,height=2,font=("arial",20,'bold'),bd=4,command= added_value.exp).grid(row=3,column=5,pady=1)
buttton_Mod=Button(Calculate,text="Mod",width=6,height=2,font=("arial",20,'bold'),bd=4,command= lambda :added_value.operate("mod")).grid(row=3,column=6,pady=1)
buttton_E=Button(Calculate,text="e",width=6,height=2,font=("arial",20,'bold'),bd=4,command=added_value.e).grid(row=3,column=7,pady=1)

buttton_Log2=Button(Calculate,text="log2",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.log2).grid(row=4,column=4,pady=1)
buttton_deg=Button(Calculate,text="deg",width=6,height=2,font=("arial",20,'bold'),bd=4,command= added_value.deg).grid(row=4,column=5,pady=1)
buttton_Acosh=Button(Calculate,text="acosh",width=6,height=2,font=("arial",20,'bold'),bd=4,command= added_value.acosh).grid(row=4,column=6,pady=1)
buttton_Asinh=Button(Calculate,text="asinh",width=6,height=2,font=("arial",20,'bold'),bd=4,command= added_value.asinh).grid(row=4,column=7,pady=1)
buttton_Log10=Button(Calculate,text="log10",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.log10).grid(row=5,column=4,pady=1)
buttton_Log1p=Button(Calculate,text="log1p",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.log1p).grid(row=5,column=5,pady=1)
buttton_Exmp1=Button(Calculate,text="exmp1",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.exmp1).grid(row=5,column=6,pady=1)
buttton_Igamma=Button(Calculate,text="lgamma",width=6,height=2,font=("arial",20,'bold'),bd=4,bg="powder blue",command= added_value.igamma).grid(row=5,column=7,pady=1)

ScienceDisplay=Label(Calculate,text="Scientific Calculator",font=("arial",30,'bold'),justify=CENTER)
ScienceDisplay.grid(row=0,column=4,columnspan=4)






root.config(menu=MenuBar)
root.mainloop()
