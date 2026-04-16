#Write a function that returns the Fibonacci series up to n terms.

# def fibonacci(n):
#     series=[]
#     a,b=0,1
#     for i in range(n):
#         series.append(a)
#         a,b=b,a+b
#     return series
# n=int(input("enter a number of trems"))
# print(fibonacci(n))
#
# print("hello")
# try:
#     x=int(input("Enter a number: "))
#     result=10/x
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("plz enter a velid number")

#try:
#     num=int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input")
# else:
#     print("you entered the number",num)
# finally:
#     print("program ended")

age=int(input("Enter an age: "))
if age<0:
    raise ValueError("age cannot be negative")
else:
     print("age is",age)
