import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
from tkinter import colorchooser
from tkinter import messagebox as mb
import pathlib
import glob
from pathlib import Path
import os
import sys
import subprocess
import shutil
import runpy


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Example")
        self.geometry("1800x900")

        self.notebook = ttk.Notebook(self)

        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)
        self.Frame3 = Frame3(self.notebook)
        self.Frame4 = Frame4(self.notebook)
        self.Frame5 = Frame5(self.notebook)
        self.Frame6 = Frame6(self.notebook)
        self.Frame7 = Frame7(self.notebook)
        self.Frame8 = Frame8(self.notebook)
        self.Frame9 = Frame9(self.notebook)
        self.Frame10 = Frame10(self.notebook)
        self.Frame11 = Frame11(self.notebook)
        self.Frame12 = Frame12(self.notebook)

        self.notebook.add(self.Frame1, text="View")
        self.notebook.add(self.Frame2, text="2")
        self.notebook.add(self.Frame3, text="3")
        self.notebook.add(self.Frame4, text="4")
        self.notebook.add(self.Frame5, text="5")
        self.notebook.add(self.Frame6, text="6")
        self.notebook.add(self.Frame7, text="7")
        self.notebook.add(self.Frame8, text="8")
        self.notebook.add(self.Frame9, text="9")
        self.notebook.add(self.Frame10, text="10")
        self.notebook.add(self.Frame11, text="11")
        self.notebook.add(self.Frame12, text="12")
        self.notebook.grid(row=0, column=0)


class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.fr1 = ttk.Frame(self)
        self.fr1.grid(row=0, column=0)
        self.fr2 = ttk.Frame(self)
        self.fr2.grid(row=0, column=1)
        self.path = "/home/jh/Desktop/PYDUMP"
        self.labelA = ttk.Label(self, text=self.path)
        self.labelA.grid(column=2, row=0)

        self.folder = self.path
        self.lb = tk.Listbox(self, bg="light blue", selectmode=tk.MULTIPLE)
        self.lb.grid(row=0, column=3, sticky="nswe")
        self.text = tk.Text(self, height=60, width=200, bg="white")
        self.text.insert("1.0", tk.END)
        self.text.grid(row=0, column=5)
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=0, column=6, sticky="nswe")
        self.scrollbar.config(command=self.text.yview)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.lb.focus()
        self.lb.configure(selectmode="")
        flist = os.listdir(self.path)
        for item in flist:
            self.lb.insert(tk.END, item)

        self.lb.bind("<<ListboxSelect>>", self.showcontent)

    def showcontent(self, evt):
        filenum = self.lb.curselection()
        self.filename = self.lb.get(filenum)
        with open(f"{self.folder}/{self.filename}", "r", encoding="utf-8") as file:
            content = file.read()
            self.text.delete("0.0", tk.END)
            self.text.insert(tk.END, content)


class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.fr1 = ttk.Frame(self)
        self.fr1.grid(row=0, column=0, columnspan=2)
        self.fr2 = ttk.Frame(self)
        self.fr2.grid(row=0, column=1)
        self.path = "/home/jh/Desktop/VERY_USEFUL_ CODE GUI_EXAMPLES__"
        self.folder = self.path
        self.labelA = ttk.Label(self, text=self.path)
        self.labelA.grid(column=2, row=0)

        self.lb = tk.Listbox(self, bg="light blue", selectmode=tk.MULTIPLE)
        self.lb.grid(row=0, column=3, sticky="nswe")
        self.text = tk.Text(self, height=60, width=200, bg="white")
        self.text.insert("1.0", tk.END)
        self.text.grid(row=0, column=5)
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=0, column=6, sticky="nswe")
        self.scrollbar.config(command=self.text.yview)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.lb.focus()
        self.lb.configure(selectmode="")
        flist = os.listdir(self.path)
        for item in flist:
            self.lb.insert(tk.END, item)

        self.lb.bind("<<ListboxSelect>>", self.showcontent)

    def showcontent(self, evt):
        filenum = self.lb.curselection()
        self.filename = self.lb.get(filenum)
        with open(f"{self.folder}/{self.filename}", "r", encoding="utf-8") as file:
            content = file.read()
            self.text.delete("0.0", tk.END)
            self.text.insert(tk.END, content)


class Frame3(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.fr1 = ttk.Frame(self)
        self.fr1.grid(row=0, column=0, columnspan=2)
        self.fr2 = ttk.Frame(self)
        self.fr2.grid(row=0, column=1)
        self.path = "/home/jh/Desktop/PYDUMP"
        self.folder = self.path
        self.labelA = ttk.Label(self, text=self.path)
        self.labelA.grid(column=2, row=0)

        self.path = "/home/jh/Desktop/PYDUMP"
        self.folder = self.path
        self.lb = tk.Listbox(self, bg="light blue", selectmode=tk.MULTIPLE)
        self.lb.grid(row=0, column=3, sticky="nswe")
        self.text = tk.Text(self, height=60, width=200, bg="white")
        self.text.insert("1.0", tk.END)
        self.text.grid(row=0, column=5)
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=0, column=6, sticky="nswe")
        self.scrollbar.config(command=self.text.yview)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.lb.focus()
        self.lb.configure(selectmode="")
        flist = os.listdir(self.path)
        for item in flist:
            self.lb.insert(tk.END, item)


class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.fr1 = ttk.Frame(self)
        self.fr1.grid(row=0, column=0)
        self.fr2 = ttk.Frame(self)
        self.fr2.grid(row=0, column=1)

        self.labelA = ttk.Label(self, text="Quick List Text Viewer")
        self.labelA.grid(column=2, row=0)

        self.path = "/home/jh/Desktop/PYDUMP"
        self.folder = self.path
        self.lb = tk.Listbox(self, bg="light blue", selectmode=tk.MULTIPLE)
        self.lb.grid(row=0, column=3, sticky="nswe")
        self.text = tk.Text(self, height=60, width=200, bg="white")
        self.text.insert("1.0", tk.END)
        self.text.grid(row=0, column=5)
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=0, column=6, sticky="nswe")
        self.scrollbar.config(command=self.text.yview)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.lb.focus()
        self.lb.configure(selectmode="")
        flist = os.listdir(self.path)
        for item in flist:
            self.lb.insert(tk.END, item)

        self.lb.bind("<<ListboxSelect>>", self.showcontent)

    def showcontent(self, evt):
        filenum = self.lb.curselection()
        self.filename = self.lb.get(filenum)
        with open(f"{self.folder}/{self.filename}", "r", encoding="utf-8") as file:
            content = file.read()
            self.text.delete("0.0", tk.END)
            self.text.insert(tk.END, content)


class Frame5(ttk.Frame):
    def __init__(self, container):
        super().__init__()

    def insertfiles(self):
        for filename in glob.glob("*.png"):
            self.lst.insert(tk.END, filename)

    def showimg(self, event):
        n = self.lst.curselection()
        filename = self.lst.get(n)
        img = tk.PhotoImage(file=filename)
        w, h = img.width(), img.height()
        print(filename)
        self.canvas.image = img
        self.canvas.config(width=w, height=h)
        self.canvas.create_image(0, 0, image=img, anchor=tk.NW)

        self.lst = tk.Listbox(self, width=20)
        self.lst.grid(row=1, column=2)
        self.lst.bind("<<ListboxSelect>>", showimg)
        insertfiles()
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=3, column=4)


class Frame6(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.fr1 = ttk.Frame(self)
        self.fr1.grid(row=0, column=0)
        self.fr2 = ttk.Frame(self)
        self.fr2.grid(row=0, column=1)

        self.labelA = ttk.Label(self, text="Quick List Text Viewer")
        self.labelA.grid(column=2, row=0)

        self.path = "/home/jh/Desktop/PYDUMP"
        self.folder = self.path
        self.lb = tk.Listbox(self, bg="light blue", selectmode=tk.MULTIPLE)
        self.lb.grid(row=0, column=3, sticky="nswe")
        self.text = tk.Text(self, height=60, width=200, bg="white")
        self.text.insert("1.0", tk.END)
        self.text.grid(row=0, column=5)
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=0, column=6, sticky="nswe")
        self.scrollbar.config(command=self.text.yview)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.lb.focus()
        self.lb.configure(selectmode="")
        flist = os.listdir(self.path)
        for item in flist:
            self.lb.insert(tk.END, item)

        self.lb.bind("<<ListboxSelect>>", self.showcontent)

    def showcontent(self, evt):
        filenum = self.lb.curselection()
        self.filename = self.lb.get(filenum)
        with open(f"{self.folder}/{self.filename}", "r", encoding="utf-8") as file:
            content = file.read()
            self.text.delete("0.0", tk.END)
            self.text.insert(tk.END, content)


class Frame7(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.fr1 = ttk.Frame(self)
        self.fr1.grid(row=0, column=0)
        self.fr2 = ttk.Frame(self)
        self.fr2.grid(row=0, column=1)

        self.labelA = ttk.Label(self, text="Quick List Text Viewer")
        self.labelA.grid(column=2, row=0)

        self.path = "/home/jh/Desktop/PYDUMP"
        self.folder = self.path
        self.lb = tk.Listbox(self, bg="light blue", selectmode=tk.MULTIPLE)
        self.lb.grid(row=0, column=3, sticky="nswe")
        self.text = tk.Text(self, height=60, width=200, bg="white")
        self.text.insert("1.0", tk.END)
        self.text.grid(row=0, column=5)
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=0, column=6, sticky="nswe")
        self.scrollbar.config(command=self.text.yview)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.lb.focus()
        self.lb.configure(selectmode="")
        flist = os.listdir(self.path)
        for item in flist:
            self.lb.insert(tk.END, item)

        self.lb.bind("<<ListboxSelect>>", self.showcontent)

    def showcontent(self, evt):
        filenum = self.lb.curselection()
        self.filename = self.lb.get(filenum)
        with open(f"{self.folder}/{self.filename}", "r", encoding="utf-8") as file:
            content = file.read()
            self.text.delete("0.0", tk.END)
            self.text.insert(tk.END, content)


class Frame8(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text="This is on Frame3")
        self.labelc.grid(column=1, row=1)


class Frame9(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text="This is on Frame3")
        self.labelc.grid(column=1, row=1)


class Frame10(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text="This is on Frame3")
        self.labelc.grid(column=1, row=1)


class Frame11(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text="This is on Frame3")
        self.labelc.grid(column=1, row=1)


class Frame12(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelc = ttk.Label(self, text="This is on Frame3")
        self.labelc.grid(column=1, row=1)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

    """


import tkinter as tk
from code.buttons import buttons
import glob

def window(self):
    "Contains all the widgets"
    
    def frame0():
        "Contains the text"
        self._frame0 = tk.Frame(self.root, bg="coral")
        self._frame0.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="nswe"
            )
        self._frame0.grid_rowconfigure(0, weight=0)
        self._frame0.grid_columnconfigure(0, weight=0)
        self._frame0.grid_columnconfigure(1, weight=0)
    
    def label_banner():
        "This is at 0,0 and occupies 2 column"
        # img = tk.PhotoImage(file=f"{self.folder}/banner.PNG")
        self.lb_banner = tk.Label(
            self._frame0,
            text=glob.glob("*book*.py")[-1],
            bg="coral")

        self.lb_banner.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="nswe"
            )

    def label_under_banner():
        "Contains the name of the file selected in the listbox on the left"
        # v. 2903 19.01.2021
        self.lb_under_banner = tk.Label(self._frame0, text=self.filename, bg="yellow")
        self.lb_under_banner.grid(
            column=0,
            row=1,
            columnspan=2,
            sticky="nswe"
            )

    def frame():
        "Contains the list of chapter names in listbox"
        self._frame = tk.Frame(self.root, bg="gray")
        self._frame.grid(column=0, row=1, sticky="nswe")
        for n in range(9):
            self._frame.grid_rowconfigure(n, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
        # self._frame.grid_columnconfigure(1, weight=1)
    
    def frame2():
        "Contains the text"
        self._frame2 = tk.Frame(self.root, bg="coral")
        self._frame2.grid(column=1, row=1, sticky="nswe" )
        self._frame2.grid_rowconfigure(0, weight=1)
        # self._frame2.grid_rowconfigure(1, weight=1)
        self._frame2.grid_columnconfigure(0, weight=1, minsize=1)
    

    def listbox():
        "The book chapter name list goes here"
        self._lbx = tk.Listbox(
            self._frame,
            bg="yellow",
            exportselection=False # To mantain the selection in the listbox when you select in the text box
            # selectmode=tk.MULTIPLE
            )
        self._lbx.grid(
            column=0,
            row=0,
            sticky="nswe"
            ) # adapt the listbox to the frame
        # self._lbx.configure(selectmode="")
        self.showlistitems()

    def scrollbars():
        self.scrollbar = tk.Scrollbar(self._frame2)
        self.scrolbar.grid(column=2, row=0,
            sticky="nswe")

    def text():
        "Contains the text of selected chapter in listbox"
        self._text = tk.Text(self._frame2, wrap=tk.WORD)
        self._text.grid(column=0, row=0, sticky="nswe")
        self._text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self._text.yview)
        
    def widgets_order():
        "The widgets on the screen"
        frame0()
        frame()
        frame2()
        label_banner()
        label_under_banner()
        listbox()
        buttons(self) # code/buttons.py
        scrollbars()
        text()
        
    widgets_order()"""
