import unittest
from unittest.mock import patch
from io import StringIO
from guess_the_number import GuessTheNumberGame

class TestGuessTheNumberGame(unittest.TestCase):

    def setUp(self):
        self.game = GuessTheNumberGame()

    @patch('builtins.input', side_effect=['1234','n'])
    def test_correct_guess(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.number = '1234'
            self.game.play_game()
            output = mock_output.getvalue().strip()
            self.assertIn("Congratulations! You guessed the number correctly.", output)
            self.assertIn("Number of attempts: 1", output)
            self.assertIn("Thank you for playing!", output)

    @patch('builtins.input', side_effect=['123a', '12345', 'abcd', '6789', '4567', '9876', 'q', '1234', 'q'])
    def test_invalid_inputs(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.play_game()
            output = mock_output.getvalue().strip()
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)
            self.assertIn("Invalid input. Please enter a valid 4-digit number.", output)

    @patch('builtins.input', side_effect=['y','q'])
    def test_play_again_yes(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.ask_to_play_again()
            output = mock_output.getvalue().strip()
            self.assertIn("Let's play another exciting round! 🎮", output)
            self.assertEqual(self.game.attempts, 0) 
        
    @patch('builtins.input', side_effect=['n'])
    def test_play_again_no(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.ask_to_play_again()
            output = mock_output.getvalue().strip()
            self.assertEqual(self.game.attempts, 0)
            self.assertEqual("Thank you for playing!",output)  
        
    @patch('builtins.input', side_effect=['invalid', 'n'])
    def test_play_again_invalid_then_yes_no(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.game.ask_to_play_again()
            output = mock_output.getvalue().strip()
            self.assertIn("Invalid input. Please enter 'y' or 'n'.", output)
            self.assertIn("Thank you for playing!",output)
            self.assertEqual(self.game.attempts, 0)  

if __name__ == '__main__':
    unittest.main()

