# Implement a program that takes 3 users  inputs from the terminal or the Browser, 
# and stores them in three variables. Return the largest of the three. 
# Do this without using the the inbuilt max () function!

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))

if num1>num2 and num1>num3:
    result=num1
elif num2>num1 and num2>num3:
    result=num2
else:
    result=num3

print(f"{result} is the largest")