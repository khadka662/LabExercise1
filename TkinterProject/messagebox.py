from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Message box')
def message():
    response= messagebox.askquestion('hello','are you robot?')
    Label(root, text=response).pack()
    if response==1:
        Label(root, text="clicked Yes").pack()
    else:
        Label(root, text="clicked No").pack()


Button(root, text="message", command=message).pack()
mainloop()
