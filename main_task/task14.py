# Write a program that takes input of 2 values and adds them.
# The program should only accept numbers and floats only or
# otherwise display an error “invalid character entered” and
# take the user to re-enter the inputs .



#while loop: will run till the condition is true.

#infinite loop
while True: 
    try:
        num1=float(input("enter first value: "))
        num2=float(input("enter second value: "))
        sum = num1 + num2
        print(sum)
        break
    except ValueError:
        print("invalid character entered")













# sumvalue=num1 + num2

# if num1==int or float and num2==int or float:
#     print(sumvalue)
# else:
#     print("Invalid Character entered")