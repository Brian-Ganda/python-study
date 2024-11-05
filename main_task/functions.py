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
  
