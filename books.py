# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def greet(self):
#         print("Hello my name is ",self.name)
#     def passed(self):
#         if(self.marks >=35):
#             return True
#         else:
#             return False
# s1=(student("John",35))
# print(s1.greet())
# print(s1.passed())

# Create a class Rectangle with:
# Attributes:
# length
# width
# Methods:
# area() → returns area of rectangle
# perimeter() → returns perimeter of rectangle
# is_square() → returns True if it is a square, else False
# Practice:
# Create 2 rectangles and print their area, perimeter, and whether they are squar

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return (self.length*self.width)
#     def perimeter(self):
#         return 2*(self.length+self.width)
#     def squre(self):
#         if self.length==self.width:
#             return ("it is squre")
#         else:
#             return("it is not squre")
# rec1=Rectangle(10,20)
# print(rec1.area())
# print(rec1.perimeter())
# print(rec1.squre())

# Library Book Class
# Task:
# Create a class Book with:
# Attributes:
# title
# author
# copies
# Methods:
# borrow() → decreases copies by 1 if available, else prints "Book not available"
# return_book() → increases copies by 1
# display() → prints "Title: <title>, Author: <author>, Copies: <copies>"
# Practice:
# Create a book object, borrow it a few times, return it, and display details each time.

class Book:
    def __init__(self,title,author,copies):
        self.title = title
        self.author = author
        self.copies = copies
    def Borrow(self):
        if self.copies > 0:
            copies = self.copies-1
            return("avilable")
        else:
            return("Book not avilable")
    def return_book(self):
        copies = self.copies+1
        return copies
    def display(self):
        print(f"{self.title} ,{self.author}, {self.copies}")
b1=Book("Python Programming","prakash ayyer",3)
print(b1.Borrow())
print(b1.return_book())
print(b1.display())

#Create a class BankAccount with name and balance. Add methods deposit(amount) and withdraw(amount).

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
account1 = BankAccount("pooja",1000)
print(account1.deposit(100))
print(account1.withdraw(100))



