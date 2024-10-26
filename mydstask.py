my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
                                                                             
#Print KES
print(my_ds[3][2]["currency"])
#Print 560
print(my_ds[2])
#rint Maths
print(my_ds[3][1])
#In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["amount"]=90
#print(my_ds)
#Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#find its index and convert it to a string
my_ds[4]=str(my_ds[4])
#reversing
my_ds[4]=my_ds[4][::-1]
#convert it back into an interger
my_ds[4]=int(my_ds[4])
#print(my_ds)
 #Hint: Strings can be reversed using [::]
 # Change the name “John” to “Jane” . 
my_ds[5]=list(my_ds[5])
my_ds[5][1]="Jane"
my_ds[5]=tuple(my_ds[5])
print(my_ds)