from tkinter import *
root=Tk()
def show():
    label= Label(root, text=var.get()).pack()
var = StringVar()
checkButton = Checkbutton(root, text="check the box!", variable=var, onvalue="on", offvalue="off")
checkButton.deselect()
checkButton.pack()

mybutton =Button(root, text="show selection",command=show).pack()
mainloop()
