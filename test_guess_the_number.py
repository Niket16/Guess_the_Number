import unittest
from unittest.mock import patch
from io import StringIO
from guess_the_number import GuessTheNumberGame

class TestGuessTheNumberGame(unittest.TestCase):

    def setUp(self):
        self.game = GuessTheNumberGame()

    @patch('builtins.input', side_effect=['123a', '12345', 'abcd', '6789', '4567', '9876', 'q', '1234', 'q'])
    def test_invalid_inputs(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.play_game()
            output = mock_output.getvalue().strip()
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)
    

    @patch('builtins.input', side_effect=['1234'])
    def test_correct_guess(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.number = '1234'
            self.game.play_game()
            output = mock_output.getvalue().strip()
            self.assertIn("Congratulations! You guessed the number correctly.", output)


if __name__ == '__main__':
    unittest.main()

