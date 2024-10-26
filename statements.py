#if statement

# if 20<30:
    # print("This is true")
    # print("This is false")

#declare a variable marks then check if the 
#marks is above 50, print pass otherwise print fail.

# marks=49
# if marks>50:
#     print("pass")
# else:
#     print("fail")

#delcare a variable num then check if the number is even or odd
# num=12
# if num%2=0:
#     print("even")
# else:
#     print("odd")
# marks=int(input("enter your marks: "))
# if marks>=80 and marks<=100:
#     print("A")
# elif marks>=70 and marks<80:
#     print("B")
# elif marks>=60 and marks<70:
#     print("C")
# elif marks>=50 and marks<60:
#     print("D")
# else :
#     print("E")


#take users age from input check if the age is greater than 60 print you are older.
#if the age is above 18 and less than 60 print you are you are an adult
# age=int(input("enter your age: "))
# if age>=60:
#     print("You are an old")
# elif age>18 and age<60:
#     print("You are an adult")
# else:
#     print("You are a child")

# task1
# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
# task2


# age=int(input("enter your age: "))
# if age>18:
#     license=input("Do you have a driving license yes/no: ")
#     if license=="yes" : 
#         print("eligible to drive")
#     else: 
#         print("Not eligible to drive")
# else: 
#     print("you are too young to drive")

# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."

creditscore=int(input("your credit score: "))
annualincome=int(input("your annual income: "))
if creditscore>700 and annualincome>50000:
    print("Loan approved")
else: 
    print("Income requirement not met")