import random

class GuessTheNumberGame:
    def __init__(self):
        self.number = str(random.randint(1000, 9999))
        print(self.number)
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
                break


if __name__ == '__main__':
    game = GuessTheNumberGame()
    game.play_game()