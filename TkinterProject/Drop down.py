from tkinter import *
root =Tk()
root.title('Drop down Menu')

def show():
    label =Label(root, text=clicked.get()).pack()
clicked =StringVar()
clicked.set("Monday")

drop =OptionMenu(root,clicked,"Monday","Tuesday","Wednesday","Thrusday","Friday","saturday","sunday")
drop.pack()
mybutton =Button(root, text="show selection", command=show).pack()
mainloop()