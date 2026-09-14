from tkinter import *
object = Tk()
"""def hello():
    print("Hello!")

btn = Button(object, text="Click Me", command = hello)
btn.pack()"""

canvas1 = Canvas(object, width = 800, height = 500)
canvas1.pack()
canvas1.create_line(400, 1, 400, 499) #Left vertical
canvas1.create_line(1, 1, 1, 499)#Middle vertical
canvas1.create_line(799, 1, 799, 499)#Right vertical
canvas1.create_line(1, 1, 799, 1) #Top horizontal
canvas1.create_rectangle(1, 1, 799, 799)

