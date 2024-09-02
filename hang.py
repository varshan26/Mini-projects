import random

words_list = ["hello", "hi", "goodbye", "goodevening", "goodnight", "cheers", "welcome", "seeyoulater", "fuckoff"]
stages = ["lives:0","lives:1","lives:2","lives:3","lives:4","lives:5"]
stages_len = len(stages)
chosen = random.choice(words_list)
chosen_len = len(chosen)

dashes = ''
for i in range(chosen_len):
    dashes += "_"

print(chosen)
print(dashes)


game = False
correct_letters = []

while not game:
    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in chosen:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen:
        stages_len -=1
        if stages_len == 0:
            game = True
            print("You lose");

    if(display == chosen):
        game = True;
        print("You won!")

    print(stages[stages_len-1]);
