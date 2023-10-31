import random

import colors

title = "Guess the number"
description = "Welcome to the world of numbers!"


def main():
    banner_str = ('    _   __           ___ \n   / | / /  _____   /__ \\\n  /  |/ /  /____/    / _/\n / /|  /  /____/ '
                  '   /_/  \n/_/ |_/            (_)   \n                         \n')
    print(colors.DARK_GREEN + banner_str + colors.RESTORE)
    print()

    score = 0
    time = 0
    number = 1
    answer = random.randint(1, 100)

    print("Welcome to the world of numbers!")
    print()

    print("The answer is between 1 to 100.")
    print("You have 50 attempts, see how many numbers you can get.")
    print()

    for attempt in range(50, 0, -1):
        guess = int(input("Please enter a number: "))
        if answer > guess:
            print("Too small!")
            time = time + 1
        elif answer < guess:
            print("Too big!")
            time = time + 1
        else:
            print()
            print("Well done, you’ve guessed the right number!")
            print()
            print("Attempts:", attempt)
            print("Score:", score)
            answer = random.randint(1, 100)
            number = number + 1
            print("Number", number, "try to get more scores.")
            score = score + (time // -2) + 25
            time = 0
    print()
    print("You have score", score, "points.")


if __name__ == '__main__':
    main()
