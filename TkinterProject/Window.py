from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('New window')

def open():
    top = Toplevel()
    top.title('check window')


    my_img = ImageTk.PhotoImage(Image.open("1.png"))
    label = Label(top, image=my_img).pack()

    button = Button(top, text="close window", command=top.destroy).pack()

button1 = Button(root, text="open", command=open).pack()
mainloop()