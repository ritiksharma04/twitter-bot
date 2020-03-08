from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title("Calculator")
root.geometry("+300+300")

#label
l1 = Label(root,text = "hello")
l1.grid(row = 0,column = 1)

#image

b1 = Button(root,text = "clr",padx = 10,pady = 10)
b1.grid(row = 1,column = 1)



root.mainloop()