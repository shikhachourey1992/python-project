#write a Python program that asks the user for their name and saves it to a file called user.txt.
#Then read the file and print the name.


name=input("enter your name:")
file=open("name.txt","w")
file.write(name)
with open("name.txt","r") as file:
    file.read()
    print(name)

#object oriented programing[oops]

class Car:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
car1=Car("Toyota","Math",'red')
car2=Car(" Alto","Palo Alto",'blue')
print(car1.brand,car1.color)
print(car2.brand,car2.color)

class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
dog1=Dog("Tom",22,1)
dog2=Dog("Tommy",12,2)
print(dog1.name,dog1.age)
print(dog2.name,dog2.weight)



