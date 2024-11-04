# Write a program that prints the largest of 4 inputs taken in from a user.
# Assume that the user would not enter any two numbers which are the same.
num1=int(input("enter number: "))
num2=int(input("enter number: "))
num3=int(input("enter number: "))
num4=int(input("enter number: "))

largenum=(num1,num2,num3,num4)
print(max(largenum))