"""
A simple number guessing game.

This module allows a user to play an interactive game where they must guess
a secret number between 1 and 99. The script provides feedback on whether the
guess is too high or too low and counts the number of attempts.
"""


import random


SECRET_NUMBER = random.randint(1,99)


def main():
    """
    A simple func to provide guessing a SECRET_MUMBER from 1 to 99.

    Returns:
        None: In succesful guessing or an exit.
    """
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck.")
    num, attempts = 0,0 
    while not num == SECRET_NUMBER:
        num = input("What's your guess between 1 and 99?\n>> ")
        attempts+=1
        if num == "exit":
            print("Goodbye!")
            return
        try:
            num = int(num)
            if num < 1 or num > 99:
                print("ERROR! Number you're guessing MUST be somewhere between 0 and 99", end=", ")
                print("try again!")
        except ValueError:
            print("That's not a number.")    

        if num == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if num > SECRET_NUMBER:
            print("Too high!")
        else:
            print("Too low!")
    print("Confratulations", end="")
    if attempts == 1:
        print("! You got it on your first try!")
    else:
        print(f", you've got it!\nYou won in {attempts} attempts!")
    return


if __name__ == "__main__":
    main()