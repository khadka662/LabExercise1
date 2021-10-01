from tkinter import *

from PIL import ImageTk, Image

root = Tk()

my_image = ImageTk.PhotoImage(Image.open("1.jpg"))
label = Label(image=my_image)
label.grid(row=2, column=0)

status = Label(root, text="Image 1 of 5")
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
button_quit = Button(root,text="Exit", command=root.quit, width=20)
button_quit.grid(row=2, column=0)
root.mainloop()
