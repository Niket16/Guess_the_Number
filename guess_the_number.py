import random

class GuessTheNumberGame:
    def __init__(self):
        self.number = str(random.randint(1000, 9999))
        # print(self.number)
        self.attempts = 0

    def play_game(self):
        while True:
            guess = input("Enter your guess (4 digits) or 'q' to quit: ")
            if guess.lower() == 'q':
             break
            if not guess.isdigit() or len(guess) != 4:
                print("Invalid input. Please enter a valid 4-digit number.")
                continue
            self.attempts += 1
            if guess == self.number:
                print("Congratulations! You guessed the number correctly.")
                print("Number of attempts:", self.attempts)
                self.ask_to_play_again()
                break

    def ask_to_play_again(self):
        self.attempts = 0
        while True:
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                self.number = str(random.randint(1000, 9999))
                # print(self.number)
                self.attempts = 0
                print("Let's play another exciting round! 🎮")
                self.play_game()
                break
            elif play_again.lower() == 'n':
                print("Thank you for playing!")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == '__main__':
    game = GuessTheNumberGame()
    game.play_game()