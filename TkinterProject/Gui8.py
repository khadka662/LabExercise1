from tkinter import *
root =Tk()

entry= Entry(root, width=50, bg="yellow", fg='orange', borderwidth=5)
entry.pack()
def click():
    textoutput= "welcome",entry.get()

    label=Label(root, text=textoutput)
    label.pack()
    button = Button(root, text="click", command=click)
    button.pack()
button = Button(root,text="click", command=click)
button.pack()

mainloop()