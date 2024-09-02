import random

rock = 0
paper = 1
scissors = 2

value = int(input("Enter a value [0=rock][1=paper][2=scissors]: "))
random_val = random.randint(0, 2)

print("computer chose: ", random_val)

if value == random_val:
    print("It's a draw")
elif (value == rock and random_val == paper) or \
     (value == paper and random_val == scissors) or \
     (value == scissors and random_val == rock):
    print("You lose")
else:
    print("You win")
