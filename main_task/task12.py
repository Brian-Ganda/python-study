# Write a program that prints the largest of 4 inputs taken in from a user.
# Assume that the user would not enter any two numbers which are the same.


def large_four(num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1>num4:
        result= "num1"
    elif num2>num1 and num2>num3 and num2 >num4:
        result= "num2"
    elif num3>num1 and num3>num2 and num3>num4:
        result= "num3"
    else:
        return num4

num1=int(input("enter number: "))
num2=int(input("enter number: "))
num3=int(input("enter number: "))
num4=int(input("enter number: "))

largest = large_four(num1,num2,num3,num4)
print(largest)










# user_input=int(input("enter number"))
# x= large_four(user_input)
# print(x)
# #   solution 1:
# # largest = max(num1,num2,num3,num4)

# user_input = num1=int(input("enter number: "))
# user_input = num2=int(input("enter number: "))
# usernum2=int(input("enter number: "))



