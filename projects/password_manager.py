from tkinter import Tk, Label, Entry, Button, messagebox
import json
import sqlite3
from password_check_generator import check_strength

#Setup the main
window = Tk()
window.title("My password vault😈😈😈")
window.config(padx=30, pady=30)


def save_password():
    website = website_entry.get().strip()
    username = user_entry.get().strip()
    password = password_entry.get().strip()
    strength = check_strength(password)
    
    if strength >= 4:
        messagebox.showwarning(title="Password strength", message= "Your password is strong!")
    elif strength >= 3:
        messagebox.showwarning(title="Password strength", message= "Your password is moderate")
    else:
        messagebox.showwarning(title="Password strength", message= "Your password is weak!(x_x)")
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message= "Please don't leave any fields empty!")
        return
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    try:
        with open("vault.json", "r") as data_file:
            data = json.load(data_file)
    except(FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    data.update(new_data)
    
    with open("vault.json", "w") as data_file:
        json.dump(data,data_file, indent=4)
    
    website_entry.delete(0, "end")
    user_entry.delete(0, "end")
    password_entry.delete(0, "end")
    messagebox.showinfo(title="Success!", message="Password saved successfully!")

def find_password():
    website = website_entry.get().strip()
    
    if len(website) == 0:
        messagebox.showwarning(
            title="Oops!",
            message="Please fill the corresponding fields"
        )
        return
    try:
        with open("vault.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showwarning(
                title = "Error!",
                message= "No saved passwords found"
                )
            return
    
    if website in data:
        username = data[website] ["username"]
        password = data[website] ["password"]

        user_entry.delete(0, "end")
        user_entry.insert(0, username)
        password_entry.delete(0, "end")
        password_entry.insert(0, password)

        messagebox.showinfo(
            title= "Password found",
            message= f"Login details for {website} have been retrieved!"
        )
    else:
        messagebox.showwarning(
            title = "Password not found",
            message= f"There is no password for {website}!"
        )

def clear():
    website_entry.delete(0, "end")
    user_entry.delete(0, "end")
    password_entry.delete(0, "end")
    return

website_label = Label(text="Website: ")
website_label.grid(row=0, column=0, sticky="e", pady=5)
user_label = Label(text="Username/Email: ")
user_label.grid(row=1, column=0, sticky="e", pady=5)
password_label = Label(text="Password: ")
password_label.grid(row=2, column=0, sticky="e", pady=5)

website_entry = Entry(width=25)
website_entry.grid(row=0, column=1, sticky="e", pady=5)
website_entry.focus()

user_entry = Entry(width=25)
user_entry.grid(row=1, column=1, sticky="e", pady=5)

password_entry = Entry(width=25, show="😈-")
password_entry.grid(row=2, column=1, sticky="e", pady=5)

save_button = Button(text="Save Password", command=save_password)
save_button.grid(row=3, column=1, pady=10)

search_button = Button(text="Search", command= find_password)
search_button.grid(row=0, column=2, padx=5)

clear_button = Button(text="Clear", command=clear) #type: ignore
clear_button.place(relx=0.01, rely=1)


window.mainloop()