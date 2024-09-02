dict = {}

turn = False

while turn is not True:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: "))
    dict[name] = price
    choice = input("any other bidder (yes or no): ")
    if (choice == "no"):
        turn = True
    else:
        print('\n'*10)

win =""
highest = 0

for i in dict:
    amount = dict[i]
    if amount > highest:
        highest = amount
        win = i


print("Highest bidder: "win)
