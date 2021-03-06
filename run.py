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

def read_guess(already_guess: Callable[[int, int], bool]) -> tuple[int, int]:
"""Guess from player"""
    while True:
        # Read row and col
        guess_row = read_int("Guess_row ", max_value=BOARD_SIZE_Y) -1
        guess_col = read_int("Guess_column ", max_value=BOARD_SIZE_X) -1
        # Valid guess return the row and column
        if not already_guessed(guess_row, guess_col):
            return guess_row, guess_col

        print("Try Again!")

def turn(board: BattleshipBoard) -> bool:
    """ Single players turn"""

    print(board.to_string())

    # Players turn to guess
    guess_row, guess_col = read_guess(board.already_guess)
    board.place_guess(guess_row, guess_col)

def play_game(player_count: int, board: BattleshipBoard) -> None:
    """ Start the game of battleship """
    os.system("clear")
    total_guesses = 0
    won_game = False

    while total_guesses < GUESSES_COUNT * player_count:
        # Current player and remaining guesses
        current_player = (total_guesses % player_count) +1
        remaining_guesses = GUESSES_COUNT - total_guesses // player_count

        print(f"Player {current_player}'s turn: {remaining_guesses} guesses left.")

        if turn(board):
            print(f"Congratulations! Player {current_player} sank the ship!")
            won_game = True
            break
        else:
            print("Sorry, you missed!")

        total_guesses += 1

        # Print the board showing the ship
    if not won_game:
        print("Game over, you didn't find the ship in time.")
    print(board.to_string(show_ship=True))

def main()