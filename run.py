import os
import random 
from typing import Callable

# Constants used for the board
GUESSES_COUNT = 5
BOARD_SIZE_X = 5
BOARD_SIZE_Y = 5

# Constants used for elements on the board
HIDDEN = "O"
SHIP = "S"
GUESS = "X"


def read_int(prompt: str, min_value: int = 1, max_value: int = 5) -> int:
"""Read an integer between a min and a max value"""

    while True:
        line = input(promt)
        try:
            value = int(line)
            if  value < min_value:
                print(f"The minimum value is {min_value}. Try again.")
            elif value > max_value:
                print(f"The maximum value is {max_value}. Try again.")
            else:
                return value
            except ValueError:
                print("Not a number! Go again.")



class BattleshipBoard

def read_guess()

def turn()

def play_game()

def main()