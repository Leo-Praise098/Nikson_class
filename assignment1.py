"""Create six string variables
    Concatenate them in pairs to fom three new variables
    Solve the following
    45 % 6 * 78 // 5 = 47
    17 // 2 ** 3 * 8 + 40 - 16 % 5 = 55
    34 * 5 + 1789 % 2 + 15 ** 2 = 396
    """

# variable1 = input("Enter a string")
# variable2 = input("Enter a second string: ")
# variable3 = input("Enter a third string: ")
# variable4 = input("Enter a fourth string: ")
# variable5 = input("Enter a fifth string: ")
# variable6 = input("Enter a sixth string: ")

# variable12 = variable1 + variable2
# variable34 = variable3 + variable4
# variable56 = variable5 + variable6

# #Use the grade and A = 70, B = 60, C = 50, D = 50, E = 40, F = 35

#score = int(input("Enter your score: "))

# if score <= 69:
#     print("Grade: D or F")
# elif score <= 79:
#     print("Grade: C")
# elif score <= 89:
#     print("Grade: B")
# else:

# if score <= 34:
#     print("Grade: F!")
# elif score <= 39:
#     print("Grade: E!")
# elif score <= 44:
#     print("Grade: D!")
# elif score <= 59:
#     print("Grade: C!")
# elif score <= 69:
#     print("Grade: B!")
# else:
#     print("Grade: A!")

# MAke the variable 9; with their multiples
# st = ""
# for number in range(1, 10):
#     print(f"---Multiples of {number}---  ")
#     for num in range(1, 6):
#         print()

for number in range(1, 10):
    print(f"Multiples of {number}")
    st_m = ""
    for num in range(1, 6):
        st = str(num * number)
        st_m  += st + "," + " "
    print(st_m)

#Checking if the lists are equal

# list1 = ["Praise", "Nikson", "Chimelem", "Okonuche", "Aseruchi"]
# list2 = ["Praise", "Nikson", "Chimelem", "Okonuche", "Aseruchi"]

# if list1 == list2:
#     list1.extend(list2)
#     print(list1)
# else:
#     print("The lists are not equal")

# #List and number manipulation

# numbers = [10, 20, 30, 40, 50]

# numbers[2] = 35
# numbers.append(60)
# numbers.remove(40)
# print(numbers)

# #List manipulation #2

# userInput = list(input("Enter a set of 5 numbers separated by space: ").split())
# print(userInput)
# userInput_int = [int(num) for num in userInput]
# print(f"The largest number is {max(userInput_int)}")
# print(f"The smallest number is {min(userInput_int)}")
# print(f"The average of the numbers are {sum(userInput_int) / len(userInput_int)}")

#Difference between remove() and discard()
"""
    Discard and remove are similar in every other way except how they act when the element is not present.
    Remove() returns a KeyError when the element is not found, but discard() returns no error if the element is not there.
    """

#Function to check if lists are equal
def list_equality(list1, list2):
    if list1 == list2:
        list1.extend(list2)
        print(list1)
    else:
        print("The lists are not equal")

#Palindrome function
def palindrome():
    word = str(input("Enter a word: ").lower())

    if word[: : -1] == word:
        print("This is a palindrome")
    else:
        print("This is not a palindrome!")

#Nested loop example into function
def nest():
    password = "1234567890"
    email = "praisewodu8@gmail.com"
    userEmail = input("Enter an email: ")
    userPassword = input("Enter your password: ")

    if userEmail == email:
        print(f"{userEmail}, you have been recognized!")
        if userPassword == password:
            print(f"Welcome {userEmail}!")
        else:
            print("Wrong password!")
    else:
        print("Your email is not recognized")

#Geopolitical zones into functions
def geo():
    userInput = input("Enter your state of origin: ")
    geopolitical_zones = {"North Central": ["Benue", "Kogi", "Kwara", "Nassarawa", "Niger", "Plateau", "FCT Abuja"], "North East": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"], "North West": ["Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Sokoto", "zamfara"], "South East": ["Abia", "Anambara", "Ebonyi", "Imo"], "South South": ["Akwa Ibom", "Bayelsa", "Cross River", "Delta", "Edo", "Rivers"], "South West": ["Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"]}
    
    
    
    for i, j in geopolitical_zones.items():
        if userInput.title() in j:
            return f"The geopolitical zone of {userInput} is {i}"

#Days calculation function
def time():
    days = float(input("Enter the number of days: "))
    years = days // 365
    rem_years = days % 365
    weeks = rem_years // 7
    rem_days = rem_years % 7
    
    return f"You have {int(years)} years, {int(weeks)} weeks, and {int(rem_days)} days left."

#Function assignment 1
def tax():
    price = float(input("Enter the price: "))
    final_price = price * ((107.5) /100)
    return final_price

#To check hypotenuse
def hypotenuse():
    adjacent = float(input("Enter the adjacent of your triangle: "))
    opposite = float(input("Enter the opposite of your triangle: "))
    hypotenuse = (adjacent**2 + opposite**2)**.5
    return hypotenuse

#How much paint is needed?
def paint():
    height = float(input("Enter the height of the wall: "))
    width = float(input("Enter the width of the wall: "))
    paint_needed = (height * width) / 10
    return paint_needed

#Checking BMI using height and weight
def BMI():
    height = float(input("Enter your height(meters): "))
    weight = float(input("Enter your weight(kg): "))
    bodyMaxIndex = weight / height**2
    return bodyMaxIndex
