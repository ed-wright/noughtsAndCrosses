"""This module currently holds the following classes:

- NoughtsAndCrosses
"""

import sys
import random

__author__ = "Edward Wright"
__version__ = "1.2.0"
__license__ = "MIT"


class NoughtsAndCrosses():
    """Contains all of the functions for noughts and crosses."""

    def __init__(self):
        """Main entry point of the app."""
        self.grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        print("Welcome to noughts and crosses")
        print("Do you want to go first or second?")
        try:
            user_input_int = int(input("Enter 1 or 2: "))
        except ValueError:
            print("You didn't enter 1 or 2")
            sys.exit()
        if user_input_int not in (1, 2):
            print("You didn't enter 1 or 2")
            sys.exit()
        if user_input_int == 1:
            self.user_turn()
        else:
            self.bot_turn()

    def user_turn(self):
        """Executes the users turn."""
        self.print_grid()
        try:
            user_row_int = int(input("Enter row between 1 and 3: "))
        except ValueError:
            print("You didn't enter a number between 1 and 3")
            sys.exit()
        if user_row_int not in (1, 2, 3):
            print("You didn't enter a number between 1 and 3")
            sys.exit()
        try:
            user_col_int = int(input("Enter column between 1 and 3: "))
        except ValueError:
            print("You didn't enter a number between 1 and 3")
            sys.exit()
        if user_col_int not in (1, 2, 3):
            print("You didn't enter a number between 1 and 3")
            sys.exit()
        grid_pos = (3 * (3 - user_row_int)) + (user_col_int - 1)
        if not 0 <= grid_pos <= 8:
            print("grid position error")
            sys.exit()
        if self.grid[grid_pos] not in ("X", "O"):
            self.grid[grid_pos] = "X"
        else:
            print("That is an invalid position")
            self.user_turn()
        self.check_win_condition()
        self.bot_turn()

    def bot_turn(self):
        """Executes the bots turn."""
        self.print_grid()
        grid_pos = random.randint(0, 8)
        if self.grid[grid_pos] not in ("X", "O"):
            self.grid[grid_pos] = "O"
        else:
            self.bot_turn()
        self.check_win_condition()
        self.user_turn()

    def print_grid(self):
        """Prints the grid with its current status."""
        print(
            "    1   2   3\n  +---+---+---+\n3 | " +
            self.grid[0] +
            " | " +
            self.grid[1] +
            " | " +
            self.grid[2] +
            " |\n  +---+---+---+\n2 | " +
            self.grid[3] +
            " | " +
            self.grid[4] +
            " | " +
            self.grid[5] +
            " |\n  +---+---+---+\n1 | " +
            self.grid[6] +
            " | " +
            self.grid[7] +
            " | " +
            self.grid[8] +
            " |\n  +---+---+---+")

    def check_win_condition(self):
        """Checks to see if the game has been won."""
        self.grid_win_check("X")
        self.grid_win_check("O")
        total_played = 0
        for element in self.grid:
            if element in ("X", "O"):
                total_played += 1
        if total_played == 9:
            print("Tie")
            self.reset_game()

    def grid_win_check(self, val):
        """Iterates through the grid looking for winning combos."""
        if self.grid[0] == val:
            if self.grid[1] == self.grid[2] == val:
                self.end_game(val)
            if self.grid[3] == self.grid[4] == val:
                self.end_game(val)
        if self.grid[8] == val:
            if self.grid[2] == self.grid[5] == val:
                self.end_game(val)
            if self.grid[6] == self.grid[7] == val:
                self.end_game(val)
        if self.grid[4] == val:
            if self.grid[1] == self.grid[7] == val:
                self.end_game(val)
            if self.grid[2] == self.grid[6] == val:
                self.end_game(val)
            if self.grid[3] == self.grid[5] == val:
                self.end_game(val)
            if self.grid[0] == self.grid[8] == val:
                self.end_game(val)

    def end_game(self, val):
        """Prints the end game message."""
        print(val + " Wins")
        self.reset_game()

    def reset_game(self):
        """Asks the user if they wish to play again, then returns the game to
        default state and goes to main or quits."""
        self.print_grid()
        result = input("Do you wish to play again? (y or n): ")
        if result == "y":
            self.grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            self.__init__()
        else:
            sys.exit()


def main():
    """This is the main entry point into the application."""
    NoughtsAndCrosses()


if __name__ == "__main__":
    main()
