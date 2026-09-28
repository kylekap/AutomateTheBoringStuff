import random

options = ["heads", "tails"]


def validate_input(guess=""):
    while guess not in options:
        print("Guess the coin toss! Enter heads or tails:")
        guess = input()
    return guess


toss = random.randint(0, 1)  # 0 is tails, 1 is heads

first_guess = validate_input()

if options[toss] == first_guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    second_guess = validate_input()
    if options[toss] == second_guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
