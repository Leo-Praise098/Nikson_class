"""
# Analogy: A bouncer at a club checking ID.
age = 20
# The condition is 'age >= 18'
if age >= 18:
    # This indented block only runs if the condition is True.
    print("Welcome! You are old enough to enter.")
print("This line runs no matter what, because it is not indented.")

temperature = 15
if temperature > 25:
    print("It's hot! Wear a t-shirt.")
else:
    # This block runs because the 'if' condition (15 > 25) is False.
    print("It's a bit chilly. You should probably wear a jacket.")

#password = "1234567890"
email = "praisewodu8@gmail.com"
userEmail = input("Enter an email: ")
#userPassword = input("Enter your password: ")

if userEmail == email:
    print(f"{userEmail}, you have been recognized!")
else:
    print("You have not been recognized")


#Second iteration
password = "1234567890"
email = "praisewodu8@gmail.com"
userEmail = input("Enter an email: ")
userPassword = input("Enter your password: ")

if userEmail == email and userPassword == password:
    print(f"{userEmail}, you have been recognized!")
else:
    print("You have been recognized")
"""

#Using the OR operator

# Level = int(input("Enter your level"))
# Permission = True

# if Level > 14 or Permission == True:
#     print("You have been granted access!")

#COndition ot check if a variable exists
# office = "Accounts"
# if office:
#     print("Welcome staff")

#Elif statement

# Analogy: Grading a student's score.
# score = int(input("Enter your score (no lying!): "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     # This runs because score >= 90 was False, but score >= 80 is True.
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# else:
#     # The final catch-all if none of the above were True.
#     print("Grade: D or F")

#Nested

# password = "1234567890"
# email = "praisewodu8@gmail.com"
# userEmail = input("Enter an email: ")
# userPassword = input("Enter your password: ")

# if userEmail == email:
#     print(f"{userEmail}, you have been recognized!")
#     if userPassword == password:
#         print(f"Welcome {userEmail}!")
# else:
#     print("Your email is not recognized")

#Using less than or equL TO

# score = int(input("Enter your score: "))

# if score <= 69:
#     print("Grade: D or F")
# elif score <= 79:
#     print("Grade: C")
# elif score <= 89:
#     print("Grade: B")
# else:

#LOOPS
#Range function
for i in range(1, 10):
    print(i)

#Nested loops
for number in range(1, 10):
    for num in range(1, 6):
        print(number * num)



#Raising my own exception
age = 15
if age < 18:
    raise ValueError("Age must be at least 18.")


try:
    # Code that may raise an exception
    pass
except SomeException:   #type: ignore
    # Handle the exception
    pass
except AnotherException:    #type: ignore
    # Handle another exception
    pass
else:
    # Runs if no exception occurred
    pass
finally:
    # Runs regardless
    pass