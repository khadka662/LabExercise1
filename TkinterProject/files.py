
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Dialog Box')



def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Downloads",
                                               title="Select a file",
                                               filetypes=(("jpg files", "*.jpg"),
                                                          ("png files", "*.png"),
                                                          ("all files", "*.*")))

    # sets the location of the selected image in the label
    my_label = Label(root, text=root.filename).pack()
    # image also gets displayed
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

mainloop()





