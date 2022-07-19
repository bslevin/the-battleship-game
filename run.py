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
                
    # Class Responsible for the Battleship Board.
class BattleshipBoard:

        # Intitailizer to create the board
    def __init__(self, size_x: int, size_y: int) -> None:
        # Create grid using list comprehension
        self.grid = [[HIDDEN] * size_x for _ in range(size_y)]

        # Ramdomly place ship on the grid 
        ship_row = random.randint(0, size_y - 1)
        ship_col = random.randint(0, size_x - 1)
        self.grid[ship_row][ship_col] = SHIP
        # If there is a ship
    def is_ship(self, row: int, col: int) -> bool:
        return self.grid[row][col] == SHIP
        # Preivious guess
    def already_guessed(self, row: int, col: int) -> bool:
        return self.grid[row][col] == GUESS
        # Method to place guess
    def place_guess(self, row: int, col: int) -> None:
        if not self.is_ship(row, col):
            self.grid[row][col] = GUESS
        # Turn the board into string representation
    def to_string(self, show_ship: bool = False) -> str:
        rows_str: list[str] = []
        for row in self.grid:
            row_repr =[HIDDEN if coll == SHIP and not show_ship else col for col in row]
            rows_str.append(" ".join(row-repr))
        return "/n".join(rows_str)
def read_guess()

def turn(board: BattleshipBoard) -> bool:
    """ Single players turn"""

    print(board.to_string())

    # Players turn to guess
    guess_row, guess_col = read_guess(board.already_guess)
    board.place_guess(guess_row, guess_col)

def play_game()

def main()