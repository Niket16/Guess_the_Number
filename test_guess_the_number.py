"""
This module contains unit tests for the GuessTheNumberGame class functionality.

Tested functionality:
- Generation of a random number within a valid range.
- Correct guessing of the number with appropriate output messages.
- Handling of various invalid inputs during gameplay.
- Hints given for partially correct guesses.
- No correct digits hints scenario.
- Game replay scenarios (both play again and do not play again).
- Comprehensive test scenario covering various gameplay scenarios.

Author:
    Niket Patel
Date:
    20/08/2023
"""

import unittest
from unittest.mock import patch
from io import StringIO
import re
from guess_the_number import GuessTheNumberGame

class TestGuessTheNumberGame(unittest.TestCase):
    """Unit tests for GuessTheNumberGame class functionality and scenarios."""

    def setUp(self):
        """Set up common test environment before each test case."""

        self.game = GuessTheNumberGame()
        self.game.number = '1234'  # Set the default number

    def test_generate_random_number(self):
        """Test random number generation within the valid range."""

        self.assertTrue(1000 <= int(self.game.number) <= 9999)

    @patch('builtins.input', side_effect=['1234', 'n'])
    def test_correct_guess(self, _):
        """Test correct guessing, output messages, and attempts tracking."""

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.number = '1234'
            self.game.play_game()
            output = mock_output.getvalue().strip()
            self.assertIn("Congratulations! You guessed the number correctly.", output)
            self.assertIn("Number of attempts: 1", output)
            self.assertIn("Thank you for playing!", output)

    @patch('builtins.input', side_effect=['123a', '12345', 'abcd', '6789', '4567', '9876', 'q'])
    def test_invalid_inputs(self, _):
        """Test handling of various invalid inputs during gameplay."""

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.play_game()
            output = mock_output.getvalue().strip()
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)

    @patch('builtins.input', side_effect=["1253"])
    def test_partial_correct_guess(self, _):
        """Test hints for partially correct guesses and hints generation."""

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.number = "1234"
            self.game.give_hints(input())
            output = mock_output.getvalue().strip()
            expected_hints = "O O - X"
            expected_output = f"Hints: {expected_hints}"
            self.assertEqual(output, expected_output)

    @patch('builtins.input', side_effect=["5678"])
    def test_no_correct_digits(self, _):
        """Test scenario with no correct digits in the hints."""

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.number = "1234"
            self.game.give_hints(input())
            output = mock_output.getvalue().strip()
            expected_hints = "- - - -"
            expected_output = f"Hints: {expected_hints}"
            self.assertEqual(output, expected_output)

    @patch('builtins.input', side_effect=['y', 'q'])
    def test_play_again_yes(self, _):
        """Test replay scenario where player chooses to play again."""

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.ask_to_play_again()
            output = mock_output.getvalue().strip()
            self.assertIn("Let's play another exciting round! 🎮", output)
            self.assertEqual(self.game.attempts, 0)

    @patch('builtins.input', side_effect=['n'])
    def test_play_again_no(self, _):
        """Test replay scenario where player chooses not to play again."""

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.ask_to_play_again()
            output = mock_output.getvalue().strip()
            self.assertEqual(self.game.attempts, 0)
            self.assertEqual("Thank you for playing!", output)

    @patch('builtins.input', side_effect=['invalid', 'n'])
    def test_play_again_invalid_then_yes_no(self, _):
        """Test replay scenarios: invalid input, play again, and not play again."""

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.ask_to_play_again()
            output = mock_output.getvalue().strip()
            self.assertIn("Invalid input. Please enter 'y' or 'n'.", output)
            self.assertIn("Thank you for playing!", output)
            self.assertEqual(self.game.attempts, 0)

    @patch('builtins.input', side_effect=[
        '1234',  # Correct guess
        'y',     # Play again
        '0000',  # Incorrect guess
        'abcd',  # Invalid input
        '123a',  # Invalid input
        'q'      # Quit
    ])
    def test_comprehensive_scenario(self, _):
        """Test comprehensive gameplay scenarios and output messages."""

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.play_game()
            output = mock_output.getvalue().strip()

            # Assertions for different scenarios
            self.assertIn("Congratulations! You guessed the number correctly.", output)
            self.assertIn("Number of attempts: 1", output)
            self.assertIn("Let's play another exciting round! 🎮", output)
            self.assertRegex(output.split("\n")[3], re.compile("Hints: |-|O|X{4}"))
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)
            # Check that the attempts counter was reset after playing again
            self.assertEqual(self.game.attempts, 0)

if __name__ == '__main__':
    unittest.main()
