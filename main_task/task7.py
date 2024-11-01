# Write that prompts the user to input student marks. 
# The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# marks=int(input("enter your marks: "))

studentmarks=int(input("what is the student Mark: "))
if studentmarks>=0 and studentmarks<=100:
    if studentmarks>=79:
        print("A")
    elif  studentmarks>=60 and studentmarks<=79: 
        print("B")
    elif studentmarks>49 and studentmarks<=59:
        print("C")
    elif studentmarks>=40 and studentmarks<=49:
        print("D")
    else:
        print("E")
else: 
    print("invalid marks")