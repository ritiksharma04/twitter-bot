from tkinter import *
root = Tk()

e = Entry(root,width= 50)   #took a entry 
e.pack()
e.insert(0,"")

def hello():
	label = Label(root, text ="hello " + e.get() )     #concatinate that entry
	label.pack()

mybutton = Button(root,text = "Click me!",command = hello) 
mybutton.pack()


root.mainloop()