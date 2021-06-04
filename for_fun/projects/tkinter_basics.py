from tkinter import *


#main 
window = Tk()
window.title("My CompSci Glossary")

#photo
photo1 = PhotoImage(file="C:\\Users\\ssubh\\OneDrive\\Pictures\\Screenshots\\andrew.jpg")
Label (window, image=photo1, bg="black").grid(row=0, coulum=0, sticky=W)


# run the main loop
window.mainloop()