#!/usr/bin/env python3
#
# Number Guessing Game!

def prompt(num):
    # Use this function to ask the user about a guess.
    # This function returns 'H', 'L', or 'C'.
    print(f"My guess: {num}")
    inp = ""
    while inp.upper() not in ['H', 'L', 'C']:
        inp = input(f"Is {num} too (H)igh, too (L)ow, or (C)orrect? ")
    return inp.upper()


def play(max):
    print(f"Think of a number from 1 to {max}.")
    input("When you're ready, press Enter.")
    low = 1
    num = (low+max)//2
    symbol = prompt(num)
    while symbol !="C":
        if symbol == "L":
            low = num
        else :
            max = num
        num = (low + max)//2
        symbol = prompt(num)
    print(num,"is the number you thought, Game over")


if __name__ == '__main__':
    play(1000)
