# Single inheritance

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Dog(Animal):
#     def bark(self):
#         print('Dog is barking')
# d=Dog('tommy', 10)
# d.bark()

#multipel inheritance

# class Father:
#     def dad(self):
#         print('Father is good')
# class Mother:
#     def mom(self):
#         print('Mother is teacher')
# class Child(Father, Mother):
#     def baby(self):
#         print('Child is baby girl')
# c=Child()
# c.dad()
# c.mom()
# c.baby()


class School:
    def maam(self):
        print("best teacher")
class collage:
    def sir(self):
        print("best sir")
class Child(School, collage):
     def student(self):
         print("student is good")

c=Child()
c.maam()
c.sir()
c.student()


#multilevel
class Grandparent:
    def grandpa(self):
        print("grandparent is good")
class Son(Grandparent):
    def Son(self):
        print("son is good")
class Grandchild(Son):
    def child(self):
        print("boy is good")
child = Grandchild()
child.grandpa()
child.Son()
child.child()






