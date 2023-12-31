# Guess the Number Game

Welcome to the **Guess the Number** game! This Python game is developed using Test Driven Development (TDD) principles to ensure a reliable and enjoyable gaming experience. In this game, your challenge is to guess a randomly generated four-digit number. The program will provide you with hints to guide you towards the correct answer. Are you up for the challenge?

## How to Play

1. **Objective**: Your goal is to guess the four-digit number generated by the program.

2. **Gameplay**:
   - The program will randomly generate a four-digit number.
   - You will repeatedly guess numbers until you guess correctly or decide to quit.
   - After each guess, the program will provide hints to help you get closer to the correct answer.
     - "O" indicates that one digit is correct and in the right spot.
     - "X" indicates that one digit is correct but in the wrong spot.
     - "-" indicates that a digit is incorrect.

3. **Example**:
   - If the randomly generated number is `7412`:
     - Your guess: `7826`
     - Hint: `O - X -`
   - Another example:
     - Your guess: `7219`
     - Hint: `O X O -`

4. **Winning**:
    - When you correctly guess the number, the program will display the number of attempts you took to win.

5. **Play Again**
    - After the game ends, you will have the option to play again or quit.
      If you choose to play again, a new randomly generated number will be presented.

6. **Quitting the Game**:
   - At any point, you can choose to quit the game. Simply enter 'q' to exit.

## Game Development Approach

This game has been developed using Test Driven Development (TDD) practices, ensuring that the game logic is robust, accurate, and ready for a captivating gaming experience.

## Get Started

1. Make sure you have Python installed on your computer.

2. Clone this repository to your local machine using:
   ```
   git clone https://github.com/your-username/guess-the-number.git
   ```

3. Navigate to the cloned directory:
   ```
   cd guess-the-number
   ```

4. Run the game by executing the following command:
   ```
   python guess_the_number.py
   ```

5. Follow the prompts to make your guesses and enjoy the game!

## Credits

This game was created with ❤️ by Niket Patel as a fun and educational project.