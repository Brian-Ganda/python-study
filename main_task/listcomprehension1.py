# it offers a concise way of creating lists from another list
# create a list of even numbers from numbers between 20 & 50.



even_numbers = [i for i in range(20,50)if i%2 == 0]
# x = list(range(20,50))
# for i in x:
#     if i%2 == 0:
#         even_numbers.append(i)

print(even_numbers)

#comprehension is a modern way of iterating through a list

# Store the square of numbers between 1 and 10
square_numbers =[i**2 for i in range(1,10)]

print(square_numbers)