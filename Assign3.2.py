print("the price of apple is 20")
apple = 20
print("the price of orange is 25")
orange = 25

def getApples(): 
    applesFunc = input("the total of apples that i want to buy: ")
    return applesFunc

def getOranges():
    orangesFunc = input("the total of oranges that i want to buy: ")
    return orangesFunc

def getAmount():
    amount = apples * apple + orange * oranges
    return amount

def displayOutpt (amount):
    print (f"the total amount is {amount}")

# Steps
# 1. ask the total apples that i want to buy and save to variable
apples = int (getApples())
#2. ask the total oranges that i want to buy and save to variable      
oranges = int (getOranges())
#3. ask the amount of the totals in apple and orange and save to variable
amount = getAmount()
displayOutpt (amount)