from tkinter import *

root = Tk()
root.title('Database GUI')
#root.iconbitmap('E:/images/global.ico')
root.geometry('300x480')

class Elder:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text = "Click ME ", command = self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("BUTTON CLICKED!!")


e = Elder(root)

root.mainloop()
