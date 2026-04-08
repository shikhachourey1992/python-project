# Polymorphism Encapsulation

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self._age=age
#     def display(self):
#         print(self.name,self._age)
# s1=Student("Rina",10)
# s1.display()
# print(s1._age)
#
# class Bankaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#     def deposite(self,ammount):
#         self.__balance+=ammount
#     def getblance(self):
#         return self.__balance
# b1=Bankaccount("Rina",500)
# b1.deposite(100)
# print(b1.getblance())
# print(b1.__balance)


#polymorphism

# class cat:
#     def sound(self):
#         return "meow"
# class dog:
#     def sound(self):ike
#         return "woof"
# c1=cat()
# print(c1.sound())
# d1=dog()
# print(d1.sound())

# class Vehicle:
#     def speed(self):
#         print("avarege speed")
# class Car(Vehicle):
#     def speed(self):
#         print("avarege speed for car 40")
# class Bike(Vehicle):
#     def speed(self):
#         print ("avarege speed for bike 60")
# for v in [Vehicle(),Car(),Bike()]:
#   v.speed()
#Q5.Make a class Human with private variable __heartbeat.Inside the class, print it.
#Try accessing it from outside — should fail.
#Q4.Make a class Phone with _battery = 80.Reduce battery by 10 in a method.
#Print updated value from outside.

# Q5.marks Create a class Laptop.Inside constructor, define _ram = 8 GB.
#Change it directly from outside.(Shows protected is not truly restricted.)

#1.Make a class Student with _marks.Create another class Topper that inherits Student.
#Print _marks from the child class.(Shows protected works in inheritance.)

# class Student:
#     def __init__(self,marks):
#         self._marks=marks
# class topper(Student):
#     def showmarks(self):
#         print(self._marks)
#
# s1=topper(45)
# s1.showmarks()

#Q3.Create a protected method _display() inside a class Animal.
#Call it from a child class Dog.

# class Animal:
#     def _display(self):
#         print("Animal")
# class Dog(Animal):
#     def _display(self):
#         print("Dog is barking")
# d1=Dog()
# d1._display()

 # Q4.Make a class Phone with _battery = 80.
# Reduce battery by 10 in a method.Print updated value from outside.

# class Phone:
#     def _battery(self):
#        self._battery =80
# class Reduce(Phone):
#     def _battery(self):
#         self._battery=+10
# b1=Reduce()
# print(b1._battery())

#Q1. Create a class BankAccount with a private variable __balance.
#  Try printing it directly — see the error.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     def deposit(self, amount):
#         self.__balance += amount
#     def get_balance(self):
#         return self.__balance
#
# B=BankAccount(500)
# print(B.deposit(100))
#print(B.__balance)
# print(B.get_balance())


#Make a class Person with a private variable __age.
#Access it using a getter method get_age().


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#     def get_age(self):
#         return self.__age
# s1=Student("John", 18)
# print(s1.name)
# print(s1.get_age())

#Q3.In a class Player, create a private attribute __score.Add a method increase_score() to add 5.
#Print final score using a method.

# class Player:
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#     def increase_score(self):
#         self.__score += 5
#         return self.__score
#
#     def final_score(self):
#         return(self.__score)
#
# p1=Player("vishu", 100)
# print(p1.name)
# print(p1.final_score())
# print(p1.increase_score())

# Q4.Create a class Bus with: private variable __seats method get_seats()
# method set_seats(value) to change seat count Use the methods to update seats.

class Bus:
    def __init__(self, seats):
        self.__seats = seats
        self.seats = 30

    def get_seats(self):
        self.__seats=-1

    def set_seats(self):
        return self.__seats
    def update_seats(self, seats):
        self.__seats =+1
        return self.__seats
b=Bus(10)
print(b.get_seats())
print(b.update_seats(10))
print(b.seats)
print(b.set_seats())














