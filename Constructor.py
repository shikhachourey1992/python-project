#  4. Advanced Constructor Use – 2 Questions
#
# Q1.Create a class Rectangle that takes length and width.Inside the constructor, calculate and store the area.
#Print the area using a method.

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         area=(self.length*self.width)
#         return (area)
# rec=Rectangle(10,20)
# print(rec.area())
# print(f"area of Rectangle is: {rec.area()}")
#

# Q2.Create a class Student that takes:
#name
# list of marks
# Inside the constructor, calculate the percentage.
# Print:
# "<name> scored <percentage>%"

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def percentage(self):
        percent=self.marks/5
        return percent
s1=Student("jhon",450)
print(f"<name:{s1.name}>,scored:<{s1.percentage()}>%")

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def percentage(self):
        total =sum(self.marks)
        percent=total/len(self.marks)
        return percent
s1=Student("Rina",[80,90,70,85,75])
print(f"<{s1.name},scored:<{s1.percentage()}>%")






