import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

print("Let's Start the game: BLACK JACK")

my_choice = []
my_choice.append(random.choice(cards))
my_choice.append(random.choice(cards))
total_mine = my_choice[0]+my_choice[1]

print("Your Cards: ",my_choice)

comp_choice = []
comp_choice.append(random.choice(cards))
comp_choice.append(random.choice(cards))
total_comp = comp_choice[0]+comp_choice[1]

print("Computer's Card: [",comp_choice[0],"]")

deal = input("Do you want to deal another card (Y/N): ").upper()

looper = True

if total_mine < 21:
    if(deal=="Y"):
        my_choice.append(random.choice(cards))
        total_mine = total_mine + my_choice[2]
        print(my_choice)
        print(comp_choice)

print("your Total: ",total_mine)
print("Computer total: ",total_comp)

if (total_mine>total_comp and total_mine<=21):
    print("You Win!")
elif(total_comp==total_mine):
    print("Draw!")
else:
    print("You Lose!")
