# Define a class Rectangle with attributes width and height.
# Add methods area and perimeter to calculate the area and perimeter of the rectangle.
# Instantiate a few rectangle objects and print their area and perimeter.
class Rectangle:
    def __init__(self,width,height):
        self.a=width
        self.b=height

    def findarea(self):
        area1 = self.a * self.b
        return area1
    
    def findperimeter(self):
        perimeter_one = (self.a + self.b) * 2
        return perimeter_one
    
myrectangle = Rectangle(5,7)
print(myrectangle.findarea())


# 2.Create a class Employee with attributes name and salary.
# Add a method give_raise that increases the salary by a given percentage.
# Instantiate an employee, give them a raise, and display their new salary.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def give_raise(self,percentage):
        self.salary += self.salary * (percentage/100)
        return f"""hello {self.name} your new salary is {self.salary}""" 
    
myemployee = Employee("Brian",500)
# myemployee.give_raise(20)
print(myemployee.give_raise(20))  




# 3.Create a base class Vehicle with attributes brand and model.
# Create two subclasses Car
# and Motorcycle that inherit from Vehicle and add unique methods to each subclass (e.g., honk for Car and rev_engine for Motorcycle).
# Instantiate both subclasses and call their methods.

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    
class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model) #calls the vehicle init method.
        self.color =color

    def honk(self):
        return f"""{self.brand}is {self.model} and is {self.color} in color and it honks."""

class Motocycle(Vehicle):
    def __init__(self,brand,model):
        super(). __init__(brand,model)
        #vehicle init method
    def rev_engine(self):
        return f"""a{self.brand} and {self.model} motorcyle revs"""
        

car1 = Car("toyota", "Crown", "red")

print(car1.honk())




# super () is used to inherit parent class methods
    # def introduce(self):
    #     return f""" Your vehicle is {self.brand} and your model is {self.model}."""
