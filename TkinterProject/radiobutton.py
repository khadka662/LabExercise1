from tkinter import*
root=Tk()
root.title("Radio Button")
MODES = [
    ("pizza", "1"),
    ("burger", "2"),
    ("momo","3"),
    ("coke","4")
]
food =StringVar()
food.set('pizza')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=food,value=mode).pack(anchor=W)

def clicked(value):
    mylabel =Label(root, text=value)
    mylabel.pack()

myButton =Button(root, text="click", command=lambda :clicked(food.get())).pack()

mainloop()
