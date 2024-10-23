#create a list of fruits
fruits = ['guava','banana','çherry','date','dingleberry']
#print(type(fruits))

# alist called days of the week
days_oftheweek= ['monday',[10,20,[100,200],30,['a','b'],40],'tuesday','wednesday','thursday','friday','saturday','sunday']
#print(days_oftheweek[1][4][1])

#modify
days_oftheweek[0]='mon'
#print(days_oftheweek)

#append
fruits = ['guava','banana','çherry','date','dingleberry','banana']

fruits.append("mango")
fruits.insert(2,"oranges")
fruits.remove("banana")
fruits.pop(0)
#print(fruits)

numbers=[1,2,3,4,5,6]
#print(numbers[0:4])

#question 1
trainees = ["John",[2,["James","Mary"]]]
print(trainees[1][0])

#question 2
trainees = ["John",[2,["James","Mary"]]]
print(trainees[1][1][0])

#question 3
trainees = ["John",[2,["James","Mary"]]]
trainees.append("56")
print(trainees)

#question 4
trainees = ["John",[2,["James","Mary"]]]
trainees[1][1].insert(1,"Mike")
print(trainees)

#question 5
#update
trainees = ["John",[2,["James","Mary"]]]
trainees[1][0] = 8
print(trainees)

#question 6 
trainees = ["John",[2,["James","Mary"]]]
trainees.remove('John')
trainees[0][1].remove("Mary")
print(trainees)
print(len(trainees))

#question 7
