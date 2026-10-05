from tkinter import Tk, Label, ttk, Button, messagebox, simpledialog
import time

toDoLists = {}
toDoLists["a"] = "Killer of time"




class toDoList:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    
    def viewTasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print(f"--------Tasks in the list {self.name}-------")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
    
    def addTask(self):
        from datetime import datetime as dt
        task = (input("Enter a new task: "))
        self.tasks.append(task)
        print(f"Task \"{task}\" added to the list!")
        reminder = input("Add a reminder for this task? (Y/N): ")
        if reminder.lower() == "y":
            reminder_time = input("Enter the reminder time (HH:MM): ")
            try:
                rem_time = dt.strptime(reminder_time, "%H:%M").time()
                print(f"Reminder set for {rem_time.strftime('%H:%M')}.")
            except ValueError:
                print("Invalid time. Please use the HH:MM format.")
        else:
            pass
        
        while dt.now().time() < rem_time:
            pass
        print("🔔 Reminder!")
    
    def removeTask(self):
        
        if not self.tasks:
            print("No tasks to remove.")
            return
        self.viewTasks()
        task_number = int(input("Enter the number of the task to be removed: "))
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task \"{removed_task}\" removed from the list.")
        else:
            print("Invalid task number!")

    def __str__(self):
        return self.name

next_id = 1

def newList():
    global next_id
    name = simpledialog.askstring("Input", "What is the name of the list?")
    name = toDoList(name)
    next_id += 1
    toDoLists[next_id] = name
    dropdown_lists["values"] = list(toDoLists.values())
    window.update()
    messagebox.showinfo(
                    title = "Success!",
                    message= f"{name} has been successfully created"
                    )

def selectList():
    if not toDoLists:
        messagebox.showwarning(
                        title = "Error!",
                        message= "No saved lists found!"
                        )
        return
    notification = Label(window, text= "yif")
    notification.place(relx=0.5, rely=0.25, anchor="center")
    
    def choice(event):
        selected = dropdown_lists.get()
        
        if selected == toDoLists.values():
            

    while True:
        print(f"--------To do List {a_list.name}-------")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
            
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter integers only!")
            
        if choice == 1:
            a_list.addTask()
        elif choice == 2:
            a_list.removeTask()
        elif choice == 3:
            a_list.viewTasks()
        elif choice == 4:
            print("Exited.")
            #break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
    
def deleteList():
    if not toDoLists:
        print("There are no lists to delete!")
        #continue
    print("\nAvailable Lists:")
    for i, toDoList in enumerate(toDoLists, start = 1):
        print(f"{i}. {toDoList.name}")
    listNum = int(input("Select a list to delete: "))
    if 1 <= listNum <= len(toDoLists):
        deleted_list = toDoLists.pop(listNum - 1)
        print(f"List \"{deleted_list.name}\" was deleted successfully!")
    else:
        print("Invalid list number!")

def Exit():
    print("Exiting the program...")
    #break
    print("Thank you for using the To-Do List program!")





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
    values= list(toDoLists.values()),
    state= "readonly"
)
dropdown_lists.bind("<<ComboboxSelected>>", choice)
dropdown_lists.place(relx=0.0675, rely=0.5, anchor="w")
dropdown_lists.current(0)

#New list button
new_list = Button(text="New list", command=newList)
new_list.place(relx=0.075, rely=0.6, anchor="w")

#Select list button
select_list = Button(text="Select List", command=selectList)
select_list.place(relx=0.075, rely=0.675, anchor="w")

#Delete list button
delete_list = Button(text="Delete List", command=deleteList)
delete_list.place(relx=0.075, rely=0.75, anchor="w")

#Exit list
exit_list = Button(text="Exit", command=Exit)
exit_list.place(relx=0.075, rely=0.825, anchor="w")



window.mainloop()