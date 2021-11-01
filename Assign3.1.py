
def getName():
    nameFunc = input("Name: ")
    return nameFunc

def getAge():
    ageFunc = input("Age: ")
    return ageFunc

def getAddress():
    addFunc = input("Address: ")
    return addFunc

def displayOutpt(nameF, ageF, addressF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addressF} .") 

# Steps
# 1. ask my name and save to variable
name = getName()
#2. ask my age and save to variable      
age = getAge()
#3. ask my address and save to variable
address = getAddress()
#4. display name,age and address
displayOutpt (name , age, address)