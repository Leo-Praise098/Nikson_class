toDoLists = []



class toDoList:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        toDoLists.append(self)
    
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

while True:
    print("\n--------To-do list--------")
    print("1. Create New List")
    print("2. Select List")
    print("3. Delete List")
    print("4. Exit")
    
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter integers only!")
    
    if choice == 1:
        name = input("Enter the name of the new list: ")
        new_list = toDoList(name)
        print(f"List \"{name}\" was created successfully!")
    elif choice == 2:
        if not toDoLists:
            print("There are no lists yet!")
            continue
        print("\nAvailable Lists:")
        for i, toDoList in enumerate(toDoLists, start = 1):
            print(f"{i}. {toDoList.name}")
        
        listNum = int(input("Select a list: "))
        a_list = toDoLists[listNum - 1]

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
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
    
    elif choice == 3:
        if not toDoLists:
            print("There are no lists to delete!")
            continue
        print("\nAvailable Lists:")
        for i, toDoList in enumerate(toDoLists, start = 1):
            print(f"{i}. {toDoList.name}")
        listNum = int(input("Select a list to delete: "))
        if 1 <= listNum <= len(toDoLists):
            deleted_list = toDoLists.pop(listNum - 1)
            print(f"List \"{deleted_list.name}\" was deleted successfully!")
        else:
            print("Invalid list number!")
    elif choice == 4:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice!")

print("Thank you for using the To-Do List program!")
