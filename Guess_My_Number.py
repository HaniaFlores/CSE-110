import random

magic_number = random.randint(1,20)

guess = -1

while guess != magic_number:
    int(input("What is your guess? "))
    
    if guess > magic_number :
        print("Lower")
    elif guess < magic_number:
        print("Higher")
    else:
        print("You guessed it!")
