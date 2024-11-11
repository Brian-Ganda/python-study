# Write a program that takes the date of birth of a person and
# the program outputs the age in terms of years,months,days TODAY.

from datetime import datetime
today = datetime.now()
print(today)

today_month = today.month
print(today_month)

today_day = today.day
print(today_day)
 
today_year = today.year
print(today_year)

dob = input("enter your date of birth(yyyy/mm/dd): ")

dob_split= dob.split("/")
years = today_year -int( dob_split[0])
months = today_month - int(dob_split[1])
days = today_day -int( dob_split[2])



print(f"{years} years,{months}months and {days}days")




# Write a program that takes input of someone's basic salary and benefits, adds them to 
# find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using 

def total_comp(a,b):
    fullcomp=a + b
    return fullcomp

basicsalary= int(input("enter your basic salary: "))
benefits= int(input("enter total benefits: "))

gross_salary= total_comp(basicsalary,benefits)
print(gross_salary)
















# age1=int(input("enter date of birth: "))
# age2=int(input("enter month of birth: "))
# age3=int(input("enter year of birth: "))

# birthday=str("age3"+"/"+"age2"+"/"+"age1")
# date= range(1,31)
# Month= range(1,12)
# year= range(2000,2024)

# for x in date:
#     if age1 <= 0 or age1> 31:
#         print('Invalid date')
#     else:
#         result=age1
# for y in Month:
#     if age2 <= 0 and age2> 12:
#         print("invalid month")
#     else: 
#         result=age2
# for z in year:
#     if age3 <=2000 and age3 > 2024:
#         result=age3
# print(f"{birthday}")

# birthday=age3+age2+age1
# print(f"my age is: {birthday}")










# Write a program that takes input of someone's basic salary and benefits, adds them to fin
# d the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
