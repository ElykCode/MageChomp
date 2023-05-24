# MageChomp magic byte reading program

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def getbytes():
    in_file = filedialog.askopenfilename()
    with open(in_file, 'rb') as open_file:
        first_bytes = open_file.read(16)
        blabel.set(first_bytes.hex(' ', 1))

root = Tk()
root.title("MageChomp")
frm1 = ttk.Frame(root, padding='3 3 10 10').grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
Label(frm1, text="MageChomp file signature reader").grid(column=0, row=1, sticky=(N,E,W))
blabel = StringVar()
Label(frm1, textvariable=blabel).grid(column=0, row=2, sticky=(N,E,W,S))
Button(frm1, text="Open File", command=getbytes).grid(column=0, row=4, sticky=(N,E,W))

root.mainloop()
