#CONSTRACTOR

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1=Student("John", 22)
print(s1.name)
print(s1.age)


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
c1=Car("BMW",21)
print(c1.brand)
print(c1.model)

class Employee:
    def __init__(self,name="unknown",age=20):
        self.name = name
        self.age = age
e1=Employee("James")
e2=Employee()
print(e1.name,e1.age)
print(e2.name,e2.age)


# Q2.
# Create a class Gadget with default constructor values for:
#
# name = “Unnamed”
# warranty = 1 year
# Print details for objects created with and without parameters.
#  4. Advanced Constructor Use – 2 Questions
#
# Q1.
#
# Create a class Rectangle that takes length and width.
#
# Inside the constructor, calculate and store the area.
#
# Print the area using a method.
#
# Q2.
#
# Create a class Student that takes:
#
# name
# list of marks
# Inside the constructor, calculate the percentage.
# Print:
# "<name> scored <percentage>%"
# Default Constructor – 2 Questions

#1. Create a class Country that uses a default constructor to print:"Welcome to the world of Geography!"
# Then create an object to trigger it.

# class Country:
#     def __init__(self):
#         print("Welcome to the world of Geography")
# c1=Country()
# print(c1)
#
# # Q2. Create a class Calculator with a default constructor that initializes a variable result to 0.
# # Print the value of result when the object is created.
#
#
# class Calculator:
#     def __init__(self):
#         print("result")
#     def multiply(self,a):
#         print(a*0)
# m1=Calculator()
# m1.multiply(2)

#  2. Parameterized Constructor – 2 Questions
# Q1. Create a class Movie with a parameterized constructor that takes:
# title
# year
# Print the movie details.

# class Movie:
#     def __init__(self,title,year):
#         self.title = title
#         self.year = year
# m1=Movie("shole",1990)
# print(m1.title,m1.year)
#
# #Create a class Mobile with a constructor that takes:
# #company
# # price
# # Print:
# # "The phone <company> costs <price>"
#
# class Phone:
#     def __init__(self,company,price):
#         self.company = company
#         self.price = price
# p1=Phone("vivo",30000)
# print(p1.company,p1.price)
# print(f"the phone {p1.company} is {p1.price}")

 #3. Constructor With Default Parameter Values – 2 Questions
#Q1. Create a class Employee with a constructor:
#__init__(self, name="Unknown", salary=0)
#Create 2 objects:
#One without passing any arguments
# One with both arguments
# Print details of both.
class Employee:
    def __init__(self,name="Unknown",salary=0):
        self.name = name
        self.salary = salary
e1=Employee()
e2=Employee("jhon",2500)
print(e1.name,e1.salary)
print(e2.name,e2.salary)

#Q2.
# Create a class Gadget with default constructor values for:
#
# name = “Unnamed”
# warranty = 1 year
# Print details for objects created with and without parameters.

class Gadget:
    def __init__(self,name="unnamed",warrenty="1year"):
        self.name = name
        self.warrenty = warrenty
g1=Gadget()
print(g1.name,g1.warrenty)








