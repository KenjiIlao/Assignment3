def getMoney_Left(): 
    money_leftFunc = input("How much money i have ")
    return money_leftFunc

def getPrice_Apple():
    price_appleFunc = input("How much is an apple: ")
    return price_appleFunc

def getApples_Amount():
    amount = money_left // price_apple
    return amount

def getMoney():
    money = money_left % price_apple
    return money  

def displayOutpt (amount, money):
    print (f"You can buy {amount} apples and your change is {money}")

# Steps
# 1. ask the money that i have and save to variable
money_left = int (getMoney_Left())
#2. ask the price of apple to buy and save to variable      
price_apple = int (getPrice_Apple())
#3. ask the total apples that i can buy and save to variable
amount = getApples_Amount()
#4. ask my change and save to variable
money = getMoney()
displayOutpt (amount,money)