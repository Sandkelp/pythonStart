from tkinter import *

window=Tk()

def km_to_mi():
    print("hello==="+e1_value.get() + "==")

    miles = float(e1_value.get()) * 1.6

    t1.insert(END,miles)

b1 = Button(window,text="Enter",command=km_to_mi)# makes a button
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)# adds a place to type

t1= Text(window,height=1,width=20)
t1.grid(row=0, column=2)# adds a text box

window.mainloop()

