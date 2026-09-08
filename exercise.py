#To display name and address in format of an envelope
def mailingAddress():
    name = "Wodu Praise Chizinorom"
    mailAddress = "praisewodu8@gmail.com"
    homeAddress = "Block F18, Redeemed close, \nNew Jerusalem Pipeline, Rukpokwu, Port Harcourt"
    print(f"{name}, \n{mailAddress} \n{homeAddress}")

#Hello with your name
def helloName():
    name = input("Enter your name: ").title()
    print(f"Hello {name}!")

#Area of a room
def areaOfRoom():
    width = float(input("Enter width of the room in meters: "))
    height = float(input("Enter height of the room in meters: "))
    print(f"The area of the room is {width * height} meters square")

#Area of a field
def areaOfField():
    width = float(input("Enter width of the field in feet: "))
    height = float(input("Enter height of the field in feet: "))
    print(f"The area of your field is {round((width * height / 43650), 4)} acres!")
    print(f"The area of your field is {(width * height / 43650):.2f} acres!")

#Vowel and Consonant checkers
def vowelConsonant():
    userInput = input("Enter an alphabet: ")
    vowels = ["a", "e", "i", "o", "u"]
    for i in userInput:
        if i in vowels:
            print(f"{i} is a vowel!")
        elif i == "y":
            print(f"{i} is sometimes a vowel and sometimes a consonant")
        else:
            print(f"{i} is a consonant!")

#COnversion to dog years
def dogYears():
    userInput = float(input("Enter the years in human: "))
    if userInput <= 2:
        print(f"{userInput} human years is equal to {userInput * 10.5} dog years")
    else:
        print(f"{userInput} human years is equal to {21 + (userInput - 2) * 7} dog years")

#Bottle deposit calculator
def bottleDeposit():
    overLitre = (input("Enter number of bottles over a litre (Type No if there is none): "))
    underLitre = (input("Enter number of bottles under a litre (Type No if there is none): "))
    if overLitre != "No":
        print(f"The refund for {overLitre} bottles is {(int(overLitre) * 0.25):.2f} $.")
    if underLitre != "No":
        print(f"The refund for {underLitre} bottles is {(int(underLitre) * 0.10):.2f} $.")

#Tax and tipping function
def taxTip():
    price = float(input("Enter the price of your meal: "))
    tip = 18% price
    valueAddedTax = 2% price
    print(f"The tax rate is 2% \nThe tip rate is 18% \nYour final payment is {price + tip + valueAddedTax}")

#Sum of first n numbers
def sumN():
    userInput = input("Enter a positive integer: ")
    if userInput[0] == "-":
        print("Please enter a positive integer!")
    else:
        userInput = int(userInput)
    sum = (userInput * (userInput + 1) / 2) #type: ignore
    print(sum)

#Widgets and gizmos
def widgetGizmo():
    widgetNum = int(input("Enter the number of widgets: "))
    gizmoNum = int(input("Enter the number of gizmos: "))
    print(f"The total weight of your order is: {widgetNum * 75 + gizmoNum * 112} grams.")

#Compound interest
def compoundInterest():
    amount = float(input("Enter the amount for savings: "))
    year1= amount * (1 + 4 / 100) **1 
    year2= amount * (1 + 4 / 100) **2 
    year3= amount * (1 + 4 / 100) **3 
    print(f"The amount after year 1 is: {year1:.2f} \nTHe amount after year 2 is: {year2:.2f} \nThe amount after year 3 is: {year3:.2f}")

#Arithmetics of two integers
def arithmetic():
    a = int(input("Enter an integer (a): "))
    b = int(input("Enter a second integer (b): "))
    import math
    print(f"The sum of integers a and b is: {a + b}. \nThe difference when b is subtracted from a is: {a - b}. \nThe product of a and b is: {a * b}. \nThe quotient when a is divided by b is: {a / b}. \nThe remainder when a is divided by b is: {a % b}. \nThe log base 10 of a is: {math.log10(a):.4f}. \nThe result of a exponential b is: {a ** b}.")

#Fuel efficiency converter
def fuel():
    american = float(input("Enter the fuel efficiency in american units (Miles per gallon): "))
    print(f"Your fuel in canadian units (Litre per 100 km) is: {american * 235.214582} L/100km")

#Distance between two places on earth
def earthDistance():
    place1 = input("Enter the latitude and longitude of location 1 separated by a blank space: ").split(" ")
    latitude1, longitude1 = float(place1[0]), float(place1[1])
    place2 = input("Enter the latitude and longitude of location 2 separated by a blank space: ").split(" ")
    import math
    latitude2, longitude2 = math.radians(float(place2[0])), math.radians(float(place2[1]))
    print(f"The distance between the locations is: {6371.01 * (math.acos(math.sin(latitude1))) + (math.sin(latitude2)) * (math.cos(latitude1)) * (math.cos(latitude2)) * (math.cos(longitude1 - longitude2))}")

#A function for change making
def changeMaker():
    cents = int(input("Enter your number of cents: "))
    #Don't understand this one yet; skip.

#Height converter
def heightConvert():
    feet = int(input("Enter your height (feet): "))
    inches = int(input("Enter your height (inches): "))
    print(f"Your height in centimeters (cm) is: {(feet * 30.48) + (inches * 2.54)} cm")

#Distance converter
def distanceConvert():
    feet = float(input("Enter a distance in feet: "))
    print(f"Your distance is equal to {feet * 12} inches. \nYour distance is equal to {feet / 3} yards. \nYour distance is equal to {feet / 5280} miles.")

#Area and volume of a circle and sphere with radius r
def circleAreaVolume():
    radius = float(input("Enter a radius: "))
    import math
    print(f"The area of a circle with your radius is {math.pi * radius**2}. \nThe volume of a sphere with your radius is {(4/3) * math.pi * radius**2}.")

#Heat conversion and cost
def heatConvertCost():
    massOfWater = float(input("Enter the mass of water in milliliters: "))
    temperatureChange =  float(input("Enter the change of temperature: "))
    energy = massOfWater * temperatureChange * 4.186
    print(f"The energy required to heat {massOfWater} milliliters of water is {energy} joules. \nThe cost of heating {massOfWater} milliliters is {(energy * 2.777e-7 * 8.9):.6f} cents")

#Volume of a cylinder
def volumeCylinder():
    height = float(input("Enter the height of the cylinder: "))
    radius = float(input("Enter the radius of the cylinder: "))
    import math
    print(f"The volume of the cylinder is: {((math.pi * radius**2) * height):.1f}")

#A function to calculate free fall
def freeFall():
    height = float(input("Enter the height of the object dropped in meters (m): "))
    import math
    print(f"The final speed of an object dropped from {height} meters is: {math.sqrt((0**2) + 2 * 9.8 * height):.4f} ms**-2; assuming acceleration due to gravity is 9.8m/s**2")

#Ideal gas laws calculations
def gasLaw():
    pressure, volume, temperature = input("Enter the pressure in pascals, volume in liters, and temperature in degrees Kelvin of the gas container; separated by spaces: ").split()
    pressure = float(pressure); volume = float(volume); temperature = float(temperature)
    print("-" * 60)
    print(f"The amount of gas moles in a container with {pressure} pascals, and a volume of {volume} liters with a temperature of {temperature} degrees Kelvin is: {(pressure * volume) / (8.314 * temperature):.4f}")

#Area of a triangle
def areaOfTriangle():
    base, height = input("Enter the base and height of the triangle separated by a blank space: ").split()
    base = float(base); height = float(height)
    print(f"The area of the triangle is: {(base * height  / 2):.4f}")

#Area of a triangle using sides of the triangle
def areaOfTriangle2():
    side1, side2, side3 =  input("Enter the sides of a triangle separated by spaces: ").split()
    side1 = float(side1); side2 = float(side2); side3 = float(side3)
    s = (side1 + side2 + side3) / 2
    import math
    print(f"The are of the triangle is: {math.sqrt(s * (s - side1) * (s - side2) * (s - side3))}")

#Area of a polygon
def areaOfPolygon():
    n, l = input("Enter the number and length of sides of a polygon, separated by a blank space: ").split()
    n = int(n); l = float(l)
    import math
    print(f"The area of a polygon with a length of {l} and {n} sides is: {(n * l**2) / (4 * math.tan(math.pi/n))}")

#Converting from days, hours, minutes, to seconds
def convertTime():
    Days = int(input("Enter the number of days: "))
    Hours = int(input("Enter the number of hours: "))
    Minute = int(input("Enter the number of minutes: "))
    Seconds = int(input("Enter the number of seconds: "))
    second = ((((Days * 24) + Hours) * 60) + Minute) * 60 + Seconds
    print(f"The number of seconds is: {second}")

#Converting from seconds to days, hours, minutes,
def convertTime2():
    seconds = int(input("Enter the number of seconds: "))
    days = seconds // 86400
    remDays = seconds % 86400
    hours = remDays // 3600
    remHours = remDays % 3600
    minutes = remHours // 60
    second = remHours % 60
    
    print(f"You have {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, and {second} seconds left.")

#Reading time using the time module
def readTime():
    import time
    print(time.mktime(time.localtime()))
    print(time.asctime())
    print(time.strftime("%a-%d-%B-%Y"))
    perf = time.perf_counter()
    mono = time.monotonic()
    start = time.perf_counter_ns()
    for i in range(1000000):
        pass
    end = time.perf_counter_ns()
    print(end - start)

#Checking BMI using height and weight
def BMI():
    height = float(input("Enter your height(meters): "))
    weight = float(input("Enter your weight(kg): "))
    bodyMaxIndex = weight / height**2
    print(bodyMaxIndex)

#Calculating wind chill
def windChill():
    temperatureAir = float(input("Enter the temperature of the air in degrees Celsius: "))
    windSpeed = float(input("Enter the speed of the wind in km/h: "))
    if windSpeed <= 4.8 or temperatureAir > 10:
        print("The wind chill is only considered valid for temperatures less than or equal to 10 degrees Celsius and wind speeds exceeding 4.8 km/h!")
    else:
        print(f"The wind chill index is: {round(13.12 + (0.6215 * temperatureAir) - (11.37 * windSpeed**.16) + (0.3965 * temperatureAir * windSpeed**.16))}")

#For converting degrees celsius or fahrenheit to kelvins
def convertKelvin():
    choice = int(input(" Choose: 1. Celsius, 2. Fahrenheit "))
    temperature = float(input("Enter your temperature: "))
    kelvins = 0
    
    def temp_fahrenheit(userInput):
        celsius = (userInput - 32) * 5 / 9
        return celsius
    
    if choice == 1:
        kelvins = temperature + 273.15
        print(f"Your temperature in kelvins is {kelvins}")
    elif choice == 2:
        kelvins = temp_fahrenheit(temperature) + 273.15
        print(f"Your temperature in kelvins is {kelvins}")
    else:
        print("Please enter a valid temperature value!")

#COnverting kilopascals to pounds per square inch, millimeter,
def convertPressure():
    kpa = float(input("Enter pressure in kilopascals: "))
    psi = kpa * 0.1450377
    mmhg = kpa * 7.50062
    atm = kpa * 0.00986923
    print(f"Pressure in psi: {psi} \nPressure in mmHg: {mmhg} \nPressure in atm: {atm}")

#Sum of digits in an integer
def sumInt():
    number = int(input("Enter a four-digit integer: "))
    digit1 = number // 1000
    digit2 = (number // 100) % 10
    digit3 = (number // 10) % 10
    digit4 = number % 10
    total = digit1 + digit2 + digit3 + digit4
    print(digit1, "+", digit2, "+", digit3, "+", digit4, "=", total)

#Sorting three integers
def sortInt():
    listOfInteger = (input("Enter three integers, separated by blank spaces: ").split())
    listOfIntegers = list(map(int, listOfInteger))
    print(type(listOfIntegers[0]))
    listOfIntegers.sort()
    print(listOfIntegers)
    print(f"The highest integer is {max(listOfIntegers)} \nThe lowest integer is {min(listOfIntegers)}")

#Discounting day old bread
def discountBread():
    number = int(input("Enter the number of day old bread u are buying: "))
    print(f"The price for Bread is $3.49, the price for day old bread is ${(60% 3.49):.2f} \nThe price for your bread is: ${(60% 3.49) * number}")

#Even or Odd
def even_odd():
    integer = int(input("Enter an integer: "))
    if integer  % 2 == 0:
        print(f"The integer \"{integer}\" is an even number")
    else:
        print(f"The integer \"{integer}\" is an odd number")

#Shape names from number of sides
def sidesShape():
    sides = int(input("Enter the number of sides of the shape(from 3 to 10): "))
    if sides not in range(3, 11):
        print("This program only supports sides of up to 10 and not less than 3!")
    else:
        if sides == 3:
            print(f"A shape with {sides} equal sides is a triangle")
        elif sides == 4:
            print(f"A shape with {sides} equal sides is a square")
        elif sides == 5:
            print(f"A shape with {sides} equal sides is a pentagon")
        elif sides == 6:
            print(f"A shape with {sides} equal sides is a hexagon")
        elif sides == 7:
            print(f"A shape with {sides} equal sides is a heptagon")
        elif sides == 8:
            print(f"A shape with {sides} equal sides is an octagon")
        elif sides == 9:
            print(f"A shape with {sides} equal sides is a nonagon")
        elif sides == 10:
            print(f"A shape with {sides} equal sides is a decagon")

#Recognizing months by their names
def months():
    nameOfMonth = input("Enter the name of the month: ")
    monthList = [""]

#Sound level
def soundLevel():
    sound = int(input("Enter a sound level in decibels: "))
    if sound == 130:
        print("Jackhammer")
    elif sound == 106:
        print("Gas lawnmower")
    elif sound == 70:
        print("Alarm clock")
    elif sound == 40:
        print("Quiet room")
    elif 106 < sound < 130:
        print("Between Gas lawnmower and Jackhammer")
    elif 70 < sound < 106:
        print("Between Alarm clock and Gas lawnmower")
    elif 40 < sound < 70:
        print("Between Quiet room and Alarm clock")
    elif sound < 40:
        print("Quieter than a quiet room")
    else:
        print("Louder than a jackhammer")

#Type of triangles based on lengths of sides
def typeTriangle():
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    side3 = float(input("Enter the third side of the triangle: "))
    if side1 == side2 == side3:
        print("The triangle is an Equilateral triangle")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is an Isosceles triangle")
    else:
        print("The triangle is a Scalene triangle")


#Frequency to notes
def frequencyToNotes():
    note = input("Enter a note: ")
    notes = {
        "C": 261.63,
        "D": 293.66,
        "E": 329.63,
        "F": 349.23,
        "G": 392.00,
        "A": 440.00,
        "B": 493.88
    }
    letter = note[0]
    octave = int(note[1])
    if letter in notes and 0 <= octave <= 8:
        frequency = notes[letter] / (2 ** (4 - octave))
        print(f"{frequency:.2f} Hz")
    else:
        print("Invalid note")

#Note To Frequencies
def noteToFrequency():
    frequency = float(input("Enter a frequency: "))
    notes = {
        "C4": 261.63,
        "D4": 293.66,
        "E4": 329.63,
        "F4": 349.23,
        "G4": 392.00,
        "A4": 440.00,
        "B4": 493.88
    }
    found = False
    for note, freq in notes.items():
        if abs(frequency - freq) <= 1:
            print(note)
            found = True
            break
    if not found:
        print("The frequency does not correspond to a known note.")