from tkinter import*
root=Tk()
Frame = LabelFrame(root, text="Frame", padx=5, pady=5)
Frame.pack(padx=10, pady=10)
button1 = Button(Frame, text="hello", padx=10, pady=10)
button1.pack(padx=50, pady=50)
button2 =Button(Frame, text="frame", padx=10,pady=10)
button2.pack(padx=30, pady=30)

mainloop()