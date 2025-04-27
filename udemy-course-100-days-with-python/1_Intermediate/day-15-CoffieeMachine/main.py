MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def checkRes(userin):
    for item in resources:
        if item in MENU[userin]["ingredients"]:
            if resources[item] < MENU[userin]["ingredients"][item]:
                return False
    return True

def pay(userin):
    cost = MENU[userin]["cost"]
    m1 = int(input("0.01 x ..."))
    m2 = int(input("0.05 x ..."))
    m3 = int(input("0.1 x ..."))
    m4 = int(input("0.25 x ..."))
    all = m1*0.01+m2*0.05+m3*0.1+m4*0.25
    if cost>all:
        print("Not enough money")
        return False
    else:
        print(f"The rest is {all-cost}")
        return True


end = True
while end:
    userin = input("What would you like? (espresso/latte/cappuccino): ")
    if userin == "off":
        end = False
    elif userin == "report":
        for item in resources:
            print(f" {item}: {resources[item]}")
    elif userin == "espresso" or userin == "latte" or userin == "cappuccino":
        enough = checkRes(userin)
        if enough:
            payOk = pay(userin)
            if payOk:

                for item in resources:
                    if item in MENU[userin]["ingredients"]:
                        resources[item] -=  MENU[userin]["ingredients"][item]
                print("Here is your latte. Enjoy!”.")

        else:
            print("Not enough resources")