# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking
# if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.

phone_num=(input("enter phone number: "))

if phone_num[0:4]=="+254" and len(phone_num)==13:
    valid=phone_num
elif phone_num[0:2]=="07" and len(phone_num)==10:
    phone_num="+254"+ phone_num[1:10]
    valid=phone_num
elif phone_num[0]=="7" and len(phone_num)==9:
    phone_num="+254" + phone_num
    valid=phone_num
elif phone_num[0:3]=="254" and len(phone_num)==12:
    phone_num="+" + phone_num
    valid=phone_num
elif phone_num[0:2]=="01" and len(phone_num)==10:
     phone_num="+254"+ phone_num[1:10]
     valid=phone_num
elif phone_num[0]=="1" and len(phone_num)==9:
     phone_num="+254" + phone_num
     valid=phone_num





print(valid)


#254702125338
# x="+254702125338"
# print(x[0:4])
# 0702125338