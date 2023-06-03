import random

Name = input("Enter your Name: ")
print("Good Luck!", Name)

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
print(word)

gusses = input("Guess the Character: ")

turns = 12

while turns > 0:

    failed = 0

    for char in word:
        if char in gusses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Won!")
        break

    print()
    guess = input("Guess a character: ")

    gusses += guess
    print(gusses)

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("you have ", + turns, "more gusses")
        if turns == 0:
            print("You loose")