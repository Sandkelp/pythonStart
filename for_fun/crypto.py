from tkinter import *

window = Tk()

#keydown function
def click():
    entered_text=e1.get()
#Coin label
l1 = Label(window, text="Coin",width=10)
l1.grid(row=0,column=0)

#price label
l2 = Label(window, text="Price", width=10)
l2.grid(row=0,column=1)

list1=Listbox(window, height=1, width=5)
list1.grid(row=1,column=0)

list2=Listbox(window, height=1, width=5)
list2.grid(row=1,column=1)

#submit button
Button(window, text="Add Symbol", width=10, command=click) .grid(row=1, column=4, sticky=W)

e1=Entry(window,width=5)
e1.grid(row=1,column=3)

window.mainloop()

