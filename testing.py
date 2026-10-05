from tkinter import Tk
from tkinter import Label
from tkinter import ttk
from tkinter import Button
import random
import time

#Creating a window and editing it
window = Tk()
window.title("Your task manager")
window.wm_attributes("-alpha", 0.875)
window.resizable(True, False)
window.minsize(700, 400)

#The heading
heading = Label(window, text="Welcome! User", font=("Arial", 15))
heading.place(relx=0.5, rely=0.08, anchor="center")

#The list label 
list_label = Label(text="Your To-Do Lists:")
list_label.place(relx=0.0675, rely=0.45, anchor="w")

#The dropdown for lists
dropdown_lists = ttk.Combobox(
    window,
    values=("Python", "Java", "C++", "JavaScript"),
    state= "readonly"
)
dropdown_lists.place(relx=0.0675, rely=0.5, anchor="w")
dropdown_lists.current(0)

#New list button
new_list = Button(text="New list")
new_list.place(relx=0.075, rely=0.6, anchor="w")

#Select list button
select_list = Button(text="Select List")
select_list.place(relx=0.075, rely=0.675, anchor="w")

#Delete list button
delete_list = Button(text="Delete List")
delete_list.place(relx=0.075, rely=0.75, anchor="w")

#Exit list
exit_list = Button(text="Exit")
exit_list.place(relx=0.075, rely=0.825, anchor="w")


#The task label
to_do_label = Label(text="Your tasks:")
to_do_label.place(relx=0.9325, rely=0.45,  anchor="e")

#The dropdown task
dropdown_tasks = ttk.Combobox(
    window,
    values= ("Python", "C++", "Javascript"),
    state="readonly"
)
dropdown_tasks.place(relx=0.9325, rely=0.5, anchor="e")
dropdown_tasks.current(0)

#Add task
add_task = Button(text="Add Task")
add_task.place(relx=0.925, rely=0.6, anchor="e")

#Remove task
remove_task = Button(text="Remove Task")
remove_task.place(relx=0.925, rely=0.675, anchor="e")

#View task
view_tasks = Button(text="View Tasks")
view_tasks.place(relx=0.925, rely=0.75, anchor="e")

#Exit tasks
exit = Button(text="Exit")
exit.place(relx=.925, rely=0.825, anchor="e")




window.mainloop()