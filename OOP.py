class Student:
    def __init__(self, Name, Department, Age, ID):
        Student.name = Name
        Student.Department = Department
        Student.Age = Age
        Student.ID = ID
    
    def __str__(self):
        return f"{Student.name} is in {Student.Department} department, aged {Student.Age}, with ID {Student.ID}."

class Mammal:

    def __init__(self, Species, howItEats):
        self.Species = Species
        self.howItEats = howItEats

class Animal:
    
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        return "Woof!"

# class Cat(Animal):
    def makeSound(self):
        return "Meow!"

class Duck(Animal):
    def makeSound(self):
        return "Quack!"

class Word:
    def convert(self):
        return "This file has been converted from a Word Document to PDF"

class AdobeReader:
    def convert(self):
        return "This file has been converted to PDF"

class Excel:
    def convert(self):
        return "This file has been converted from an .xlsx document to PDF"

class PowerPoint:
    def convert(self):
        return "This file has been converted from a .pptx to PDF"

def display(name):
    print(name.convert())


Excel1 = Excel()
Word1 = Word()
AdobeReader1 = AdobeReader()
PowerPoint1 = PowerPoint()

class AudioFile:
    def open_file(self):
        return "Playing MP3 audio track..."

class VideoFile:
    def open_file(self):
        return "Streaming MP4 video at 2160p..."

class ImageFile:
    def open_file(self):
        return "Rendering JPEG image on screen..."

a_video = VideoFile()
an_image = ImageFile()
an_audio = AudioFile()

a_list = [a_video, an_image, an_audio]

for i in a_list:
    print(i.open_file())


#FOr abstract classes
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass

class PaystackPayment(PaymentProcessor):
    
    def process_payment(self):
        print(f"Processing ${self.amount} securely via Paystack API Webhook")

class BankTransferPayment(PaymentProcessor):
    
    def process_payment(self):
        print(f"Generating temporary dynamic account number for ${self.amount} transfer via Bank API")

class StudentFees:
    fees = 150000
    
    def __init__(self, student_name, fees):
        self.student_name = student_name
        self.__fees = fees
    
    
    def check_balance(self):
        print(f"Your balance is: {self.__fees}")
    
    def make_payment(self, amount):
        if amount > 0:
            self.__fees -= amount    
            print(f"Payment of ${amount} made successfully. Remaining balance: ${self.__fees}")
        else:
            print("Enter a valid amount!")
student = StudentFees("John Doe", 150000)
student.check_balance()
student.make_payment(50000)