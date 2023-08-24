"""
    This module defines the GuessTheNumberGame class, which is a simple number guessing game.
    Players attempt to guess a 4-digit number randomly chosen by the computer.

    The game provides hints to guide the player towards the correct answer.

    Usage:
        Run this module directly to play the Guess The Number game.

    Author:
        Niket Patel

    Date:
        20/08/2023
"""

import random
# import time


class GuessTheNumberGame:
    """Number guessing game for 4-digit numbers."""

    def __init__(self):
        self.number = str(random.randint(1000, 9999))
        # print(self.number)
        self.attempts = 0

    # Print in typing effect in CLI
    # def print_typing_effect(self, text, delay=0.01):
    #     for char in text:
    #         print(char, end='', flush=True)
    #         time.sleep(delay)
    #     print()

    @staticmethod
    def print_game_intro():
        """Prints game introduction with rules and hints for the Guess The Number game."""

        print("=============================================================")
        print("                     GUESS THE NUMBER GAME                   ")
        print("=============================================================")
        print("Welcome, brave challenger!")
        print("Can you crack the code and reveal")
        print("the secret 4-digit number?")
        print("You'll receive hints after each guess.")
        print("Legend:")
        print("     O - Correct digit in correct position")
        print("     X - Correct digit in wrong position")
        print("     - - Incorrect digit")
        print("=============================================================")

    def play_game(self):
        """Play the number guessing game, providing hints and tracking attempts."""

        self.print_game_intro()

        while True:
            guess = input("Enter your guess (4 digits) or 'q' to quit: ")
            if guess.lower() == 'q':
                print("\nOh no, you've decided to leave the challenge...")
                print(f"But wait, the secret number you were after is: {self.number}!")
                self.attempts = 0
                break
            if not guess.isdigit() or len(guess) != 4:
                print("Invalid input. Please enter a valid 4-digit number.")
                continue
            self.attempts += 1
            self.give_hints(guess)
            if guess == self.number:
                print("Congratulations! You guessed the number correctly.")
                print("Number of attempts:", self.attempts)
                self.ask_to_play_again()
                break

    def give_hints(self, guess):
        """Generate and display hints for the guessed number."""
        hints = []
        for i, digit in enumerate(guess):
            if digit == self.number[i]:
                hints.append('O')
            elif digit in self.number:
                hints.append('X')
            else:
                hints.append('-')
        if len(hints) == 0:
            print("No digits are correct.")
        else:
            if " ".join(hints) != "O O O O":
                print("Hints:", " ".join(hints))

    def ask_to_play_again(self):
        """Reset game or exit based on player's choice."""

        self.attempts = 0
        while True:
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                self.number = str(random.randint(1000, 9999))
                self.attempts = 0
                # print(self.number)
                print("Let's play another exciting round! 🎮")
                self.play_game()
                break
            if play_again.lower() == 'n':
                print("Thank you for playing!")
                break
            print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == '__main__':
    GAME = GuessTheNumberGame()
    GAME.play_game()
