from tkinter import *
from tkinter import filedialog
import os

filepath = None

def open_file():
    global filepath
    filepath = filedialog.askopenfilename()
    print(filepath)
    selected.config(text=filepath)

def convert_file(arg):
    global filepath
    if '.' not in choice.get():
        choice.after(200, lambda:choice.config(bg="#ed431c"))
        choice.after(1000, lambda:choice.config(bg="#c2c2c2"))
        return
    arg = os.path.splitext(arg)[0]
    arg = arg + choice.get()

    os.rename(filepath, arg)
    filepath = arg
    selected.config(text=filepath)


root = Tk()
root.geometry("480x240")
root.resizable(False, False)

open = Button(root, text="hehe", command=open_file)
open.pack(pady=10)

selected = Label(root, text="nothing")
selected.pack()

choice = Entry(root, bg="#c2c2c2")
choice.pack(pady=20)

convert = Button(root, text="convert", command=lambda: convert_file(filepath))
convert.pack()

root.mainloop()