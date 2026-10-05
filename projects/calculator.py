from tkinter import Tk, Label, Button, messagebox, Entry, Frame

#Designing the window
root = Tk()
root.title("Calculator")
root.wm_attributes("-alpha", 0.875)
root.resizable(True, False)
root.minsize(350, 500)



#Functions for the buttons

def calculate(event=None):
    try: 
        result = space.get()
        answer = eval(result)
        space.delete(0, "end")
        under_space = Entry(
            interface,
            font=("Garamond", 16),
            justify="right",
            cursor="xterm"
        )
        under_space.place(relx=.05, rely=.5, relwidth=.9, relheight=.40)
        under_space.insert("end", answer)
        root.after(1000, under_space.destroy)#Never use sleep(500). It freezes the window
    
    except ZeroDivisionError as zero:
        space.delete(0, "end")
        messagebox.showerror(
            title="Division by zero",
            message= f"You have an error, {zero}"
        )
    except SyntaxError:
        space.delete(0, "end")
        messagebox.showerror(
            title="Invalid expression",
            message= "Invalid expression!"
        )
    except ValueError:
        space.delete(0, "end")
        messagebox.showerror(
            title= "Invalid value",
            message= "Invalid value!"
        )
    except NameError:
        space.delete(0, "end")
        messagebox.showerror(
            title= "Invalid value",
            message= "Invalid value!"
        )

    except TypeError:
        space.delete(0, "end")
        messagebox.showerror(
            title= "Invalid value",
            message= "Invalid value!"
        )

def blankspace(event=None):
    space.insert("end", " ")

def clear(event=None):
    space.delete(0, "end")

def backspace(event=None):
    space.delete((len(space.get()) - 1))

def input_dot(event=None):
    space.insert("end", ".")

def input_division(event=None):
    space.insert("end", "/")

def input_multiplication(event=None):
    space.insert("end", "*")

def plus(event=None):
    space.insert("end", "+")

def minus(event=None):
    space.insert("end", "-")

def input_0(event=None):
    space.insert("end", 0)

def input_1(event=None):
    space.insert("end", 1)

def input_2(event=None):
    space.insert("end", 2)

def input_3(event=None):
    space.insert("end", 3)

def input_4(event=None):
    space.insert("end", 4)

def input_5(event=None):
    space.insert("end", 5)

def input_6(event=None):
    space.insert("end", 6)

def input_7(event=None):
    space.insert("end", 7)

def input_8(event=None):
    space.insert("end", 8)

def input_9(event=None):
    space.insert("end", 9)

#The interface for calculations display
interface = Label(
    root, 
    font=("Georgia", 20),
    fg="olive",
    anchor="center",
    justify="right",
    padx=.5,
    pady=.1,
    cursor="hand2"
)
interface.place(relx=0.5, rely=0.01, relwidth=0.925, relheight=0.25, anchor="n")

#Container for all buttons
container = Frame(
    root,
    bd=3
)
container.place(relx=0.0125, rely=0.275, relwidth=0.975, relheight=0.7)


#Number 0
number_0 = Button(container, text="0",
    command=input_0,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_0.place(relx=0.28, rely=.76, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-0>", input_0)

#Number_(.)
button_dot = Button(container, text=".",
    command=input_dot,
    font=("Garamond", 30), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
button_dot.place(relx=0.52, rely=.76, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-period>", input_dot)

number_1 = Button(container, text="1",
    command=input_1,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_1.place(relx=0.04, rely=.52, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-1>", input_1)

number_2 = Button(container, text="2",
    command=input_2,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_2.place(relx=0.28, rely=.52, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-2>", input_2)

number_3 = Button(container, text="3",
    command=input_3,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_3.place(relx=0.52, rely=.52, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-3>", input_3)

number_4 = Button(container, text="4",
    command=input_4,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_4.place(relx=0.04, rely=.28, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-4>", input_4)

number_5 = Button(container, text="5",
    command=input_5,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_5.place(relx=0.28, rely=.28, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-5>", input_5)

number_6 = Button(container, text="6",
    command=input_6,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_6.place(relx=0.52, rely=.28, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-6>", input_6)

number_7 = Button(container, text="7",
    command=input_7,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_7.place(relx=0.04, rely=.04, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-7>", input_7)

number_8 = Button(container, text="8",
    command=input_8,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_8.place(relx=0.28, rely=.04, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-8>", input_8)

number_9 = Button(container, text="9",
    command=input_9,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
number_9.place(relx=0.52, rely=.04, relwidth= 0.2, relheight= 0.2)
root.bind("<Key-9>", input_9)

button_backspace = Button(container, text="⌫",
    command=backspace,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
button_backspace.place(relx=0.76, rely=.04, relwidth= 0.2, relheight= 0.144)
root.bind("<BackSpace>", backspace)

button_plus = Button(container, text="+",
    command=plus,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
button_plus.place(relx=0.76, rely=.2048, relwidth= 0.2, relheight= 0.104)
root.bind("<Key-plus>", plus)

button_minus = Button(container, text="-",
    command=minus,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
button_minus.place(relx=0.76, rely=.3296, relwidth= 0.2, relheight= 0.104)
root.bind("<Key-minus>", minus)

button_division = Button(container, text="/",
    command=input_division,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
button_division.place(relx=0.76, rely=.4544, relwidth= 0.2, relheight= 0.104)
root.bind("<Key-slash>", input_division)

button_multiplication = Button(container, text="*",
    command=input_multiplication,
    font=("Garamond", 20),
    bg="azure",
    cursor="hand2",
    relief="raised",
    anchor="center",
    activeforeground="white"
)
button_multiplication.place(relx=.76, rely=.5792, relwidth= 0.2, relheight= 0.104)
root.bind("<Key-asterisk>", input_multiplication)

button_equals = Button(container, text="=",
    command=calculate,
    font=("Garamond", 20), 
    bg="azure",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
button_equals.place(relx=0.76, rely=.76, relwidth= 0.2, relheight= 0.2)
root.bind("<Return>", calculate)

#The clear button
button_C = Button(container, text="C",
    command=clear,
    font=("Garamond", 20), 
    fg="#47C322",
    bg="#FFF8E7",
    cursor="hand2", 
    relief="raised", 
    anchor="center",
    activeforeground="white"
)
button_C.place(relx=0.04, rely=.76, relwidth= 0.2, relheight= 0.2)
root.bind("<Delete>", clear)


space = Entry(
    interface,
    font=("Garamond", 16),
    justify="right",
    cursor="xterm"
)
space.place(relx=.05, rely=.05, relwidth=.9, relheight=.40)
root.bind("<space>", blankspace)


root.mainloop()