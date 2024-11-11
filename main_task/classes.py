
#define a class name car.
# shape, size , the brand , color
# .append()


# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color= color

#     def describe(self):
#         return f"""The car in the alley is {self.brand} and it's {self.color} in color."""
    
# #create object
# alleycar = Car("Benz", "Blue")
# print(alleycar.describe())












class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
            return self.num1 +self.num2
    def subtraction(self):
         return self.num1 - self.num2
    def multiplicaiton(self):
         return self.num1 * self.num2
    def division(self):
         return self.num1/self.num2
    
operation1 = Calculator(1000,500)
print(operation1.add())














# class Car:
#     #constructor 
#     def __init__(self,color,shape,brand):
#         self.color=color
#         self.brand=brand
#         self.shape=shape
    

#     def describe(self):
#         return f"""the color of the car is {self.color} and the brand is {self.brand} and the shape is {self.shape}"""
    

# #create object
# my_car = Car("red","benz","wagon")
# print(my_car.describe())
# print(my_car.brand)

# #question two:
# class Student:
#     #constructor
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    

#     def introduce(self):
#         return f"""Hello, my name is {self.name} and I am {self.age} years old."""
    
# student_one = Student("Brian", "100")
# print(student_one.introduce())
    

# class Calculator:
#     def __init__(self,a,b):
#         self.a = a + b
#         self.b = a - b
#         self.c = a * b
#         self.d = a / b

#     def introduce(self):
#         return f"""if you add the two numbers you get {self.a} but if you subtract the two numbers you get {self.b} and if you decide to multiply the two numbers you get {self.c} and lastly if you divide both numbers you get 
#         {self.d}."""

# mycalculator = Calculator(5,2)
# print(mycalculator.introduce())

    

# 1.Create a class Animal with attributes species and sound.Add a method make_sound that prints: "The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.

class Animal:
    def __init__(self,species,sounds):
        self.x = species
        self.y = sounds

    def describe(self):
        return f"""The {self.x} goes {self.y}!"""
    
make_sound = Animal("Lions","roar")
print(make_sound.describe())

        



# # 2.Create a class Book with attributes like title, author, and year.
# # Add a method that returns a description of the book.
# # Create an object of Book and print out the description.

class Book:
    def __init__(self,title,author,year):
        self.v = title
        self.r = author
        self.m = year
    
    def introduce(self):
        return f"""The title of your book is the {self.v}, the author is {self.r} and it was written in the year {self.m}"""

fake_book = Book("Bible","Jesus","2000")
print(fake_book.introduce())



# # 3.Define a class BankAccount with attributes owner and balance (set balance to 0 by default).Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
# # Ensure that the withdraw method does not allow the balance to go negative.

class BankAccount:
    def __init__(self,owner,balance,):
        self.z = owner
        self.d = balance

    def deposit(self):
        def deposits_money(x):
            if x > 0:
                return f""" Thank you {self.z} for depositing {x}"""
    def withdrawal(self):
        def withdraws_money(x):
            v = 0
            v = self.d - x
            return f"""You {self.z} have withdrawn{v}"""
    def get_balance(self):
            v = 0
            r = self.d - v
            return f"""your new balance is {r}"""


    # def introduce(self):
    #     return f"""Thank you {self.z} for depositing {}. Your balance is {self.d}

myaccount = BankAccount("Brian", 5000)
print(myaccount.get_balance())
