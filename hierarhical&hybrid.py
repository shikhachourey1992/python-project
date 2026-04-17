# Create a class Writer with method write(). Create a class Singer with method sing().
# Create a class Artist that inherits both and can call both methods.
#Create classes Animal → Mammal → Human.
# Animal: breath()
#  Mammal: walk()
# Human: think()
# Call all using Human object.

# class Animal:
#     def breath(self):
#         print('I am breathing')
# class Mammal:
#     def walk(self):
#         print('I am walking')
# class Human(Animal, Mammal):
#     def think(self):
#         print('I am thinking')
# h1=Human()
# h1.breath()
# h1.walk()
# h1.think()
#
#
# class Writer:
#     def write(self):
#         print('I am writing')
# class Singer:
#     def sing(self):
#         print('I am singing')
# class  Artist(Writer, Singer):
#     def art(self):
#         pass
# a1=Artist()
# a1.sing()
# a2=Writer()




#HIERARHICAL INHERITANCE

# class Animal:
#     def ani(self):
#         print("name")
# class Dog(Animal):
#     def ani1(self):
#         print("age ")
# class Cat(Animal):
#     def ani2(self):
#         print("hello")
# class Cow(Animal):
#     def ani3(self):
#         print("hey")
# d1=Dog()
# d1.ani1()
# c1=Cat()
# c1.ani2()
# c2=Cow()
# c2.ani3()
# d1.ani()

# class Employee:
#     def compny(self):
#         print('Compny method')
# class Manager(Employee):
#     def manage  (self):
#         print("manage compny")
# class Developer(Employee):
#     def develop(self):
#         print("developer")
# m1=Manager()
# m1.compny()
# m1.manage()
# d1=Developer()
# d1.develop()
# d1.compny()


#  HYBRID INHERITANCE

# class A:
#     def a(self):
#         print('A show')
# class B(A):
#     def b(self):
#         print('B show')
# class C(A):
#     def c(self):
#         print('C show')
# class D(B,C):
#     def d(self):
#         print('D show')
# d1=D()
# d1.a()
# d1.b()
# d1.c()
# d1.d()

# Person
#
#    /    \
#
# Teacher  Student
#
#     \    /
#
#  TeachingAssistant
#
# Device
#
#    /     \
#
# Laptop   Tablet
#
#     \    /
#
#   HybridDevice

# class Person:
#     def man(self):
#         print("man is good")
# class Teacher(Person):
#     def maam(self):
#         print("maam is teaching")
# class Student(Person):
#     def boy(self):
#         print("boy is student")
# class TeachingAssistant(Teacher, Student):
#     def school(self):
#         print("school")
# t1=TeachingAssistant()
# t1.man()
# t1.boy()
# t1.school()
# t1.maam()
#

# class Device:
#     def machine(self):
#         print("Handmade machine")
# class Laptop(Device):
#     def lapee(self):
#         print("Lapee is Laptop")
# class Tablet(Device):
#     def tab(self):
#         print("Tab is Tablet")
# class Hybrid(Laptop, Tablet):
#     def hybrid(self):
#         pass
# hybrid_device = Hybrid()
# hybrid_device.machine()
# hybrid_device.lapee()
# hybrid_device.tab()
#
# class Animal:
#     def ani(self):
#         print("Animal is dengers")
# class Mammal(Animal):
#     def ani2(self):
#         print("Mammal is dengers")
# class Bird(Animal):
#     def ani3(self):
#         print("Bird is flying")
# class FlyingMammal(Mammal, Bird):
#     def bluebird(self):
#         print("bluebird is flying")
# flyb=FlyingMammal()
# flyb.ani()
# flyb.ani2()
# flyb.ani3()
# flyb.bluebird()
#
