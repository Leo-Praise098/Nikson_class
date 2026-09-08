path = ""

# with open("output.txt", "x") as file:
#     file.write("Hello World!")

with open("output.txt", "w") as file:
    file.write("Hello World!")
#The r before the string means raw string, which helps prevent backslashes from being interpreted as escape sequences.
path =  r"C:\Users\USER\OneDrive\Documents\MISCELLANEOUS\Nickson's class\output.txt"
with open(path) as file:
    content = file.read()
print(content)

# with open("testing.csv", "x") as file:
#     file.write("Hello, World!")
#     file.readline()
#     file.readlines() Returns the lines in the file as a list of strings
#     file.writelines() To write multiple lines to a file, you can use the writelines() method. This method takes a list of strings as an argument and writes each string to the file as a separate line.

with open(r"C:\Users\USER\OneDrive\Documents\MISCELLANEOUS\NIckson's class\testing.csv", "r+") as file:
    content = file.read()
    file.write("\nYou are invited to be a part of the learning process here at tequant resources!")
    print(content)

file = open("students.txt", "r")

#The traditional method of opening a file and closing it after use is as follows:
try:
    content = file.read()

    # Something goes wrong here

finally:
    file.close()

#Exercise 1: File handling
name = input("Enter your name: ")
food = input("Enter your favorite food: ")
with open("orders.txt", "w") as file:
    pass

with open("orders.txt", "a") as file:
    file.write(f"Hello {name}, your favorite food is {food}.")

with open("orders.txt", "r") as file:
    content = file.read()
    print(content)

#Exercise 2: Error handling
try:
    cost = int(input("Enter the cost of the whole box: "))
    items = int(input("Enter how many items are in the box: "))
    price_per_item = cost / items
    print(f"The price per item is: ${price_per_item}")
except ValueError:
    print("Please enter only the amount in numbers!")
except ZeroDivisionError:
    print("Please enter a valid number of items in the box!")
finally:
    print("Thank you for shopping with us!")