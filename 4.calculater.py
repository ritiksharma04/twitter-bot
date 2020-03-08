from tkinter import *
root = Tk()
root.title("Simple calculater")

#space for entry
e = Entry(root,width = 35,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 5,padx = 10,pady = 10)


#defining operaters
def button_click():
	e.delete(0,END)
	e.insert(0,number)
#creating button
button_1 = Button(root,text = "1",padx = 10,pady = 10,command = lambda: button_click(1))
button_2 = Button(root,text = "2",padx = 10,pady = 10,command = lambda: button_click(2))
button_3 = Button(root,text = "3",padx = 10,pady = 10,command = lambda: button_click(3))
button_4 = Button(root,text = "4",padx = 10,pady = 10,command = lambda: button_click(4))
button_5 = Button(root,text = "5",padx = 10,pady = 10,command = lambda: button_click(5))
button_6 = Button(root,text = "6",padx = 10,pady = 10,command = lambda: button_click(6))
button_7 = Button(root,text = "7",padx = 10,pady = 10,command = lambda: button_click(7))
button_8 = Button(root,text = "8",padx = 10,pady = 10,command = lambda: button_click(8))
button_9 = Button(root,text = "9",padx = 10,pady = 10,command = lambda: button_click(9))
button_0 = Button(root,text = "0",padx = 10,pady = 10,command = lambda: button_click(0))

#special button
button_equal = Button(root,text = "=",padx = 50,pady = 20)
button_clear = Button(root,text = "clr",padx = 50,pady = 20)
button_add = Button(root,text = "+",padx = 50,pady = 20)
#put button on screen
button_1.grid(row = 3,column =1 )
button_2.grid(row = 3,column = 2)
button_3.grid(row = 3,column =3 )

button_4.grid(row = 2,column = 1)
button_5.grid(row = 2,column = 2)
button_6.grid(row = 2,column = 3)

button_7.grid(row = 1,column = 1)
button_8.grid(row = 1,column = 2)
button_9.grid(row = 1,column = 3)

button_0.grid(row = 4,column =1  )

button_add.grid(row = 1,column = 4)
button_clear.grid(row = 2,column = 4)
button_equal.grid(row = 4,column = 1)


root = mainloop()