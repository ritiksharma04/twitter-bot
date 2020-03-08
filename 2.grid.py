from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Hello World!")   #CREATING THE THINGS
myLabel2 = Label(root, text = "I am Ritik Sharma")

myLabel1.grid(row = 0,column = 0)  #PUTTING THAT IN SCREEN
myLabel2.grid(row = 1,column = 1)

root.mainloop()
