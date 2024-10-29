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

# creditscore=int(input("your credit score: "))
# annualincome=int(input("your annual income: "))
# if creditscore>700 and annualincome>50000:
#     print("Loan approved")
# else: 
#     print("Income requirement not met")

# TASK ONE
#1.Take three inputs from a user, separately. Print the largest of the numbers.
    # Hint: Determine what type of data is taken in as input.
#question 1 
mathscore=float(input("what is your math score: "))
sciencescore=float(input("what is your science score: "))
englishscore=float(input("what is your english score: "))

#method one: max(function)
largest=max(mathscore,sciencescore,englishscore)
print(f"The largest number is {largest}")   

#method two:
if mathscore>sciencescore and mathscore>englishscore:
     largest=mathscore
elif sciencescore>mathscore and sciencescore>englishscore:
     largest=sciencescore
else: 
     largest=englishscore
print(f"the largest number is {largest}")
#formatted strings=>used to pass variables inside strings
name="john"
age=25
#my name is john and my age is 25
print(f"my name is:{name} and my age is:{age}")
#2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
Temperature=int(input("what is the temperature of the room: "))
if Temperature>=30:
    print("The temperature is too high")
elif Temperature>=15 and Temperature<30:
    print("Normal Temperature")
else:
    print("cold temperature")
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x = 16  
y = 190 

if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password=input("what is the password: ")
if password=="secret123":
     print("Access Granted")
else: 
     print("Access Denied")

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=int(input("what is the student score: "))
if student_score>90 and student_score>80:
     print("Excellent Student")
else: 
     print("Good score,but attendance needs improvement")


#strip because of spaces and add the lower so as to convert directly to lowercase the account type 
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
transactionamount=float(input("what is the transaction amount: "))
accounttype=str(input("what is the account type: ")).strip().lower()
if accounttype=="standard":
     if transactionamount>500:
          print("Transaction exceeds the limit for Standard accounts.")
     else: 
        print("Transaction approved.")
elif accounttype=="premium":
     if transactionamount>1000:
          print("Transaction exceeds the limit for premium accounts.")
     else:
          print("Transaction approved.")



# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."
