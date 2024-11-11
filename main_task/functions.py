#a function to calculate the area of a triangle
# area=1/2 *b*h

def area_triangle():
    base=10
    height=20
    area=(1/2)*base*height
    print(area)

area_triangle()


#area of a rectangle

def area_rectangle():
    length=50
    width=100
    area=length*width
    print(area)

area_rectangle()


#using params and arguments
def area_tri(base,height):
    area=(base*height)*0.5
    print(area)

area_tri(20,10)
area_tri(100,50)


#a function to calculate the area of rectangel using parameters

def area_rectangle(length,width):
    area=length*width
    return area

y= area_rectangle(10,20)
print(y)


#create a function to check if a number is even or odd

def even_num(num):
    if num%2==0: 
        result = "even number"
    else:
        result="odd number"
    return result

user_input=int(input("enter number"))
x= even_num(user_input)
print(x)
  

def sum_marks(a,b,c,d,e):
    totalmarks= a + b + c + d + e
    return totalmarks

math=int(input("enter maths marks: "))
eng=int(input("enter eng marks: "))
swa=int(input("enter swa marks: "))
sci=int(input("enter sci marks: "))
sos=int(input("enter sos marks: "))


x = sum_marks(math,eng,swa,sci,sos)
print(x)


#calculate the average

def calc_average(tm,num):
    average= tm/num
    return average

marks_average=calc_average(x,5)
print(marks_average)

#find the grade

def find_grade(avg):
    if avg>79:
        grade="A"
    elif avg>60 and avg<=79:
        grade="B"
    elif avg>49 and avg<=59:
        grade="C"
    elif avg>40 and avg<=49:
        grade="D"
    else:
        grade="E"
    return grade

mygrade=find_grade(marks_average)
print(mygrade)



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

def find_nhif(z):
    if z <= 5999:
        rate = "150"
    elif z > 6000 and z <= 7999:
        rate = "300"
    elif z > 8000 and z <= 11999:
        rate = "400"
    elif z > 12000 and z <=14999:
        rate ="500"
    elif z > 15000 and z <= 19999:
        rate = "600"
    elif z > 20000 and z <= 24999:
        rate = "700"
    elif z > 25000 and z <=29999:
        rate ="800"
    elif z > 30000 and z <=34999:
        rate ="900"
    elif z > 35000 and z <= 39999:
        rate = "950"
    elif z > 40000 and z <= 44999:
        rate = "1000"
    elif z > 45000 and z <=49999:
        rate ="1100"
    elif z > 50000 and z <=59999:
        rate ="1200"
    elif z > 60000 and z <= 69999:
        rate = "1300"
    elif z > 70000 and z <= 79999:
        rate = "1400"
    elif z > 80000 and z <= 89999:
        rate ="1500"
    elif z > 90000 and z <= 99999:
        rate = "1600"
    elif z > 100000:
        rate = "1700"
    return rate


myrate=find_nhif(gross_salary)
print(myrate)




