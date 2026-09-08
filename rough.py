# # name = int(input("eNTER YOUR NAME: "))
# # print(name)

# # if type(name) == int:
# #     print("Error: Your name cannot be an integer")

# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # for i in numbers:
# #     print(f"Numbers {i}")

# # adjectives = ["red", "big", "tasty"]
# # fruits = ["apple", "cucumber", "bread"]
# # for adj in adjectives:
# #     for fruit in fruits:
# #         print(adj, fruit)

# # a_List = [1, 2, "Tayo", ]

# # myList = []
# # for i in myList:
    

# # f = [3, 5, 9, 5, 20, 4]
# # sum = 0
# # f.sort

# # for i in f:
# #     sum += i
# # mean = sum / len(f)
# # print(sum, mean)

fName = ["bola", "nnamdi", "ben", "philly", "gabby"]
# lName = ["teddy", "juan", "uli", "amadi", "uriel"]
# for i in lName:
#     fName.append(i)
# print(fName)

# print(fName.pop())
# lName.pop()

# for i in fName:
#     print(i.capitalize())
# for i in lName:
#     print(i.capitalize())

# mylist = ["apple", "banana", "cherry", "mango", "kiwi"]

# a_names = [i for i in mylist if "a" in i]
# except_apple = [i for  i in mylist if "apple" and "kiwi"  not in i]
# print(except_apple)
# print(mylist.reverse())
# integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]

# word = str(input("Enter a word: ").lower())

# if word[: : -1] == word:
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome!")

# a_tuple = (10, 20)
# print(a_tuple[0])

studentRecord = ("Praise", 18, 5.8, True)
studentRecord = studentRecord + (4,)
print(studentRecord)
# name, age, height, attendance = studentRecord
# print(name)
# print(type(studentRecord))

# a_set = {"apple", "banana", "cherry", "dingoes"}
# a_set.add("Cucumber")
# print(a_set)
# print(a_set.pop())
# print(a_set)
# a_frozen =  frozenset([1, 2])
# print(a_frozen)

a_dict = {"Name": "Praise Chizinorom Wodu", "University": "Babcock University",}
# print(a_dict.keys())
# print(a_dict.values())
print(a_dict.get("Name", "No name key"))
# if a_dict["Name"] == "Praise Chizinorom Wodu":
#     print("Yes!")
# print(a_dict.items())

userInput = input("Enter your state of origin: ")


geopolitical_zones = {"North Central": ["Benue", "Kogi", "Kwara", "Nassarawa", "Niger", "Plateau", "FCT Abuja"], "North East": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"], "North West": ["Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Sokoto", "zamfara"], "South East": ["Abia", "Anambara", "Ebonyi", "Imo"], "South South": ["Akwa Ibom", "Bayelsa", "Cross River", "Delta", "Edo", "Rivers"], "South West": ["Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"]}


for i, j in geopolitical_zones.items():
    if userInput in j:
        print(f"The geopolitical zone of {userInput} is {i}")
    else:
        print("Wrong State of origin")

# import math
# print(math.pi)





def temperature():
    userInput = float(input("Enter your temperature: "))
    fahrenheit = (userInput * 9 / 5) + 32 
    return f"Your temperature is {int(fahrenheit)} degrees Fahrenheit"

def temp_fahrenheit(userInput):
    celsius = (userInput - 32) * 5 / 9
    return celsius

def temp_kelvin():
    choice = int(input(" Choose: 1. Celsius, 2. Fahrenheit "))
    temperature = float(input("Enter your temperature: "))
    kelvins = 0
    if choice == 1:
        kelvins = temperature + 273.15
    elif choice == 2:
        kelvins = temp_fahrenheit(temperature) + 273.15
    else:
        print("Please enter a valid temperature value!")
    return int(kelvins)

print(f"Your temperature in kelvins is {temp_kelvin()} kelvins!")