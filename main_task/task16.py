#  Write a program that takes input of someone's basic salary and benefits, adds them to fin
# d the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  


def total_comp(a,b):
    fullcomp=a + b
    return fullcomp

basicsalary= int(input("enter your basic salary: "))
benefits= int(input("enter total benefits: "))

gross_salary= total_comp(basicsalary,benefits)
print(gross_salary)

def find_nhif(z):
    if z <= 5999:
        rate = "150"
    elif z > 6000 and z <= 7999:
        rate = "300"
    elif z > 8000 and z <= 11999:
        rate = "400"
    elif z > 12000 and z <=14999:
        rate ="500"
    elif z > 15000 and z <= 19999:
        rate = "600"
    elif z > 20000 and z <= 24999:
        rate = "700"
    elif z > 25000 and z <=29999:
        rate ="800"
    elif z > 30000 and z <=34999:
        rate ="900"
    elif z > 35000 and z <= 39999:
        rate = "950"
    elif z > 40000 and z <= 44999:
        rate = "1000"
    elif z > 45000 and z <=49999:
        rate ="1100"
    elif z > 50000 and z <=59999:
        rate ="1200"
    elif z > 60000 and z <= 69999:
        rate = "1300"
    elif z > 70000 and z <= 79999:
        rate = "1400"
    elif z > 80000 and z <= 89999:
        rate ="1500"
    elif z > 90000 and z <= 99999:
        rate = "1600"
    elif z > 100000:
        rate = "1700"
    return rate


myrate=find_nhif(gross_salary)
print(myrate)


# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary.
# BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 

def find_nssf(x):
    if x < 18000:
        rate = "Not applicable"
    elif x > 18000:
        rate = float(x)*0.06
    return rate

nssfrate=find_nssf(gross_salary)
print(nssfrate)




# # Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
def find_ndhf(f):
    myndhf = float(f) * 0.015
    return myndhf

nhdfamount=find_ndhf(gross_salary)
print(nhdfamount)

# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

def find_vat(e,f,g,h):
    myvat = float(e) - (f + g + h)
    return myvat


nssf1=int(input("enter your nssf: "))
nhdf1=int(input("enter your nhdf: "))
nhif1=int(input("enter your nhif: "))

taxable_income=find_vat(gross_salary,nssf1,nhdf1,nhif1)
print(taxable_income)


# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK

def find_paye(m):
    m = 0
    if m <24000:
        result = float(m) * 0.01
    elif m < 32333:
        result = float(m) * 0.25
    elif m < 500000:
        result = float(m) * 0.30
    elif m < 800000:
        result = float(m) * 0.325
    elif m  < 16000000:
        result = float(m) * 0.35
        return result
    
payeeformular = int(input("enter your taxable income: "))
mypayee = find_paye(payeeformular)
print(mypayee)
    


