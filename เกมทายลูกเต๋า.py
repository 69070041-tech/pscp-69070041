"""Dice Guessing Game Checker"""


def main():
    """start function"""
    guess = int(input())
    real = int(input())

    if guess < 1 or guess > 6 or real < 1 or real > 6:
        print("Invalid")
    elif guess == real:
        print("Correct!")
    else:
        print("Wrong!")

main()
