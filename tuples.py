marks=(100,130,160,190,200)
print(marks)
#print(type(marks))

#convert the tuple into a list
marks=list(marks)
#(type(marks))

#modify
marks[2]=1000
#print(marks)
#convert it back into a tuple again
marks=tuple(marks)
#print(type(marks))

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
print(days[2])
#2. Using a function a find the length of the tuple.
print(len(days))
#3. Replace Thursday with Thur
days=list(days)
print(type(days))
days[3]="Thur"
print(days)

days=tuple(days)
print(type(days))


