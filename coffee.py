MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0,
        },
        "cost":20,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":50,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":80,
    },
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0,
}

def checker2(a):
    a = a
    if(resources["coffee"]<MENU[a]["ingredients"]["coffee"]):
        print("We are low on coffeee")
        state = False
    if(resources["milk"]<MENU[a]["ingredients"]["milk"]):
        print("we are low on milk")
        state = False
    if(resources["water"]<MENU[a]["ingredients"]["water"]):
        print("we are low on water")
        state = False
    else:
        print("We have enough resources!")
        coins(a)

def coins(a):
    a = a
    print("Enter the coins needed----->")
    tens = int(input("Enter the no of tens : "))
    twentys = int(input("Enter the no of twentys: "))
    fiftys = int(input("Enter the no of fiftys: "))
    total = (tens*10)+(twentys*20)+(fiftys*50)
    costed = MENU[a]["cost"]
    change = total - costed

    if(total>=costed):
        print("Yes the amount is sufficient!")
        making(a,costed)
        if(total>costed):
            print("Here is the extra change: ",change)
    else:
        print("Nope, the amout is not sufficient!")
        state = False


def making(a,add):
    print("-----ENJOY YOUR COFFEE!!------")
    resources["coffee"] -= MENU[a]["ingredients"]["coffee"]
    resources["milk"] -= MENU[a]["ingredients"]["milk"]
    resources["water"] -= MENU[a]["ingredients"]["water"]
    resources["money"] += add
    print("remaining resources: ",resources)



state = True

while state:
    choice = input("What would you like? (espresso,latte,cappuccino) :").lower()
    if(choice=="espresso"):
        print("your choice is Espresso!")
        checker2(choice)
    elif(choice=="latte"):
        print("your choice is Latte!")
        checker2(choice)
    elif(choice=="cappuccino"):
        print("Your choice is Cappuccino!")
        checker2(choice)
    elif(choice=="off"):
        state = False
    elif(choice=="report"):
        print(resources)
