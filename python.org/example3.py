#example from python website
from tkinter import *

root = Tk()

li  =["hello","deadpool",1,3,4]

listb = Listbox(root)

for item in  li:
    listb.insert(0,item)

listb.pack()
root = mainloop()
