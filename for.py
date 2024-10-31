# fruits=["apple","banana","mangoes"]
# for fruit in fruits:
#     if fruit == "mangoes":
#         print(fruit)



#range()= its used to create a list of numbers

# numbers=list(range(0,101))
# print(numbers)

#iterate through numbers from 10 to 40
# x=list(range(10,41))
# for number in x:
#     print(number)

#iterate through numbers from 10 to 50 and only display even numbers:
# even_num=[]
# x=list(range(10,51))
# for number in range(10,51):
#     if number % 2==0:
#         even_num.append(number)

# print(even_num)

# question 2:
# prime_num=[]
# y=list(range(1,51))
# for number in range(1,51):
#     if number % 7 == 0 or number % 5 == 0:
#         prime_num.append(number)

# print(prime_num)

# question 3:


# v=list(range(10,40))
# numero= sum(range(10,40))
# averagenum= int(sum(range(10,41))/len(range(10,41)))
# print(f"Sum of numbers between 10 to 40: {numero}")
# print(f"Average of numbers between 10 to 40 is: {averagenum}")

#kevins answer:
# v=list(range(10,40))
# sm=0
# for i in v:
#     sm=sm+i
#     average=sm/len(v)
# print(sm)
# print(average)



#question 3:

# # oddnum=list(range(10,50))
# emptylist=[]
# count=0
# for number in oddnum:
#     if number % 2 !=0:
#         emptylist.append(number)
#         count=count+1
#         if count==10:
#             break
    
# print(emptylist)


#question 5:
num = int(input("enter number: "))

for i in range(10):
        mult=num*i
        print(f'{num}*{i} = {mult}')
        

#question 6:
numlist=list(range(1,50))
even_count=0
for x in numlist:
        if  x%2 == 0:
                even_count+=1
print(even_count)


#question 7:
# Display the total quantity of the 3 above.

ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32), ("bread", 100) ]
total_quantity=0

for i in ls1:
        quantity=i[1]
        total_quantity+=quantity

print(total_quantity)





