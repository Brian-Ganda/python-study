my_set = {10,20,30,40,50}
print(type(my_set))
print(my_set)
print(my_set)

#set methods

my_set.add(60)
print(my_set)

#remove
my_set.remove(40)
print(my_set)

days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
days.remove("friday")
days.remove("sunday")
print(days)
#Add them back to the set
days.add("friday")
days.add("sunday")
print(days)



#Remove friday and sunday from the set using methods.
