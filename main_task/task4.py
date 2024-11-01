# Write a program which accepts email as form input or from terminal.
#  Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email_address=input("enter email: ")
if "@"  in email_address and "." in email_address:

    print("valid email")

else:
    print("invalid email")


#regular expressions: used to check the format