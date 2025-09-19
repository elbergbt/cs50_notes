import random
import sys

def main():
    random_number = get_random()

    while True:
        guess_number = get_guess()
        if guess_number < random_number:
            print("Too small!")
        elif guess_number > random_number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_random():

    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            else:
                number = random.randint(1, level)
                return number

        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess_number = int(input("Guess: "))
            if guess_number <= 0:
                raise ValueError
            else:
                return guess_number

        except ValueError:
            pass
main()