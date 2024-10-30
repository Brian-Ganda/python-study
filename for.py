fruits=["apple","banana","mangoes"]
for fruit in fruits:
    if fruit == "mangoes":
        print(fruit)



#range()= its used to create a list of numbers

numbers=list(range(0,101))
print(numbers)

#iterate through numbers from 10 to 40
# x=list(range(10,41))
# for number in x:
#     print(number)

#iterate through numbers from 10 to 50 and only display even numbers:
even_num=[]
x=list(range(10,51))
for number in range(10,51):
    if number % 2==0:
        even_num.append(number)

print(even_num)
