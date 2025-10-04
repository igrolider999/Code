from tkinter import *
from tkinter import filedialog
import os
import subprocess

filepath = None
widgets = {}


def open_file(page):
    global filepath
    selected = widgets[page]["selected"]
    filepath = filedialog.askopenfilename()
    print(filepath)
    selected.config(text=filepath)

def open_folder(page):
    global filepath
    selected = widgets[page]["selected"]
    filepath = filedialog.askdirectory()
    print(filepath)
    selected.config(text=filepath)

def convert_file(page, arg):
    global filepath
    choice = widgets[page]["choice"].get()
    selected = widgets[page]["selected"]
    if '.' not in choice:
        root.after(200, lambda:choice.config(bg="#ed431c"))
        root.after(1000, lambda:choice.config(bg="#c2c2c2"))
        return
    arg = os.path.splitext(arg)[0]
    arg = arg + choice

    os.rename(filepath, arg)
    filepath = arg
    selected.config(text=filepath)

def open_explorer():
    try:
        subprocess.Popen(f'explorer /select,"{os.path.normpath(filepath)}"')
    except:
        return

def switch_page(page):
    if page == "page1":
        widgets["page1"]["frame"].place_forget()
        page2_init()
    elif page == "page2":
        widgets["page2"]["frame"].place_forget()
        page1_init()

root = Tk()
root.geometry("480x240")
root.resizable(False, False)

def page1_init():
    pagename = "page1"

    page1 = Frame(root)
    page1.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)
    Label(page1, text="Thas paje 1").pack()

    open = Button(page1, text="hehe", command=lambda: open_file(pagename))
    open.pack(pady=10)

    selected = Button(page1, text="nothing", command=open_explorer, relief="flat")
    selected.pack()

    choice = Entry(page1, bg="#c2c2c2")
    choice.insert(0, '.')
    choice.pack(pady=20)

    convert = Button(page1, text="convert", command=lambda: convert_file(pagename, filepath))
    convert.pack()

    switch = Button(page1, text="paje2", command=lambda: switch_page(pagename))
    switch.pack()

    widgets[pagename] = {
        "frame": page1,
        "open": open,
        "selected": selected,
        "choice": choice,
        "convert": convert
    }

def page2_init():
    global current_page
    pagename = "page2"
    current_page = 2

    page2 = Frame(root)
    page2.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)
    Label(page2, text="Das is page2").pack()

    open = Button(page2, text="hehe", command=lambda: open_folder(pagename))
    open.pack(pady=10)

    selected = Button(page2, text="nothing", command=open_explorer, relief="flat")
    selected.pack()

    choice = Entry(page2, bg="#c2c2c2")
    choice.insert(0, '.')
    choice.pack(pady=20)

    convert = Button(page2, text="convert", command=lambda: convert_file(pagename, filepath))
    convert.pack()

    switch = Button(page2, text="page1", command=lambda: switch_page(pagename))
    switch.pack()

    widgets[pagename] = {
        "frame": page2,
        "open": open,
        "selected": selected,
        "choice": choice,
        "convert": convert
    }

page1_init()
root.mainloop()