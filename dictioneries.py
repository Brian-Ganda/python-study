person={
    'name': "brian",
    'age': 24,
    'gender': 'male',
    'location': ['kiambu',518,'thika'],
    'address':{
    'street':'mombasa road',
    'city':'nairobi',
    'country':'kenya' 
   }
}
print(type(person))

print(person['age'])
print(person['gender'])
print(person['location'][0])
print(person['location'][2])
print(person['address']['city'])
print(person['address']['country'])

#note that when you  use the key to go the value you want, now you apply by the rules of that specific data structure
#adding properties
person['occupation']='doctor'
print(person)

#update properties
person['age']= '50'
print(person)
#phone number
person['phone number']='070234567'
print(person)

#dictionery
print(person.keys())
#.values() = returns all the values belonging to that dictionery
print(person.values())

#.items() = returns a list containing a tuple of each key and a value.
print(person.items())

#.pop() = removes property of a specified key
person.pop('address')
print(person)

#.popitem() = removes the last item added to the dictionery
person.popitem()
print(person)

#.clear()
person.clear()
print(person)