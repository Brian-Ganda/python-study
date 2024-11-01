# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, 
# display  either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.

# solution:
whole_num=int(input("enter number: "))
if whole_num % 2 == 0:
        print("even")
elif whole_num % 2 != 0:
        print("odd")



# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.
# whole_num=int(input("enter number: "))
if whole_num % 4 == 0:
        print("divisible by 4")
else: 
        print("not divisible by 4")

      

