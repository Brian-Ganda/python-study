# Write that prompts the user to input student marks. 
# The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# marks=int(input("enter your marks: "))

def grading_system(studentmarks):
    result=""
    if studentmarks>=79:
        result="A"
    elif  studentmarks>=60 and studentmarks<=79: 
        result="B"
    elif studentmarks>49 and studentmarks<=59:
        result="C"
    elif studentmarks>=40 and studentmarks<=49:
        result="D"
    else:
        result="E"
        return result

y=grading_system(grade)
print(y)
# a function takes in some data perfoms some operation on thta data and must give an output.












# studentmarks=int(input("what is the student Mark: "))
