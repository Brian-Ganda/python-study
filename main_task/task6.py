# Write a program that lets the user input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”.
# If the password is correct access is granted.
# After you show them a message , the account is blocked.
correct_pwd= "admin123"
attempts=4
x=range(0,4)
for i in x:
    pwd=input("enter password: ")
    if pwd == correct_pwd: 
        print("Access is granted")
        break
    else :
        remaining_attempts=attempts - (i+1)
        print(f"wrong password you have {remaining_attempts} remaining attemps")
        if remaining_attempts == 0:
            print("Account Blocked")




