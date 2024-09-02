import random

numbers = list(range(1,101))

choice = random.choice(numbers)

print("Welcome to the number guessing game!: ")
print("Im thinking of a Number from 1 to 100: ")
difficulty = input("Choose a Difficulty (easy/hard): ").lower()

attempts = 0

if(difficulty == "easy"):
    attempts +=10
    print("You have ",attempts," attempts!")
elif(difficulty == "hard"):
    attempts += 5
    print("You have ",attempts," attempts!")
else:
    print("Wrong input!")

print("computer's number: ",choice)

while attempts != 0:
    guess = int(input("Make a guess: "))

    if(guess>choice):
        print("Too high, Guess again!")
        attempts-=1
        print("You have ",attempts," attempts!")
    elif(guess<choice):
        print("Too Low, Guess again!")
        attempts-=1
        print("You have ",attempts," attempts!")
    elif(guess == choice):
        print("Correct guess!")
        temp = False
    else:
        print("Wrong input, Guess again!")
        attempts-=1
        print("You have ",attempts," attempts!")
