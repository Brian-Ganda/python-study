name=" JOHn ."
#replace the dot with an empty space
#strip to remove spaces at the start and at the end
#convert to lowercase
name=name.replace(".",(""))
name=name.strip()
name=name.lower()
print(name)

#question 2:
sentence_one="The Dog Breed is German Shepherd"
print(sentence_one[8:23])

#question 2(b):
sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

#question 3:

#split with a semi colon
text="The lazy dog; ran so fast; it hit the wall."
text=text.split(";")
print(text)
print(len(text))

#question 4:

#first you strip to remove the spaces,for first name and last name
#replace the dot with a string
#finally you add the two names
first_name=" Joh.n"
last_name=" Do,e"
first_name=first_name.strip()
last_name=last_name.strip()

first_name=first_name.replace(".","")
last_name=last_name.replace(",","")
fullname=first_name+" "+last_name
print(fullname)


 # for number 5 you use the string method .replace

r= '["E","W","C]'
r=r.replace(",", "")
r=r.replace("[","")
r=r.replace('"', "")
r=r.replace("]", "")
print(r)
