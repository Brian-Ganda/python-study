# Write a program that takes the email and password as input from a user and
# checks if they are equal to “admin@mail.com” and password is “Admin@123” ,
# if so then print  “Login is Successful” and if not print “Invalid username or password”.
#  ONLY accept 3 tries after which it notifies you that you have been blocked.
# username=(input("enter email: "))
# password=(input("enter password: "))


realemail="admin@gmail.com"
realpassword="Admin@123"

attempts=3
x=range(0,3)
for i in x:
    username=input("enter email: ")
    password=(input("enter password: "))

    if username == realemail and password == realpassword: 
        print("Access is granted")
        break
    else :
        print("Invalid Username or password")
        remaining_attempts=attempts - (i+1)
        print(f"wrong password you have {remaining_attempts} remaining attemps")
        if remaining_attempts == 0:
            print("Account Blocked")


