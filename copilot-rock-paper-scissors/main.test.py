import unittest
from io import StringIO
from unittest.mock import patch
from main import determine_winner, play_game


class TestGame(unittest.TestCase):
    def test_determine_winner_tie(self):
        result = determine_winner("rock", "rock")
        self.assertEqual(result, "It's a tie!")

    def test_determine_winner_user_wins(self):
        result = determine_winner("rock", "scissors")
        self.assertEqual(result, "You win!")

    def test_determine_winner_computer_wins(self):
        result = determine_winner("rock", "paper")
        self.assertEqual(result, "The computer wins!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_tie(self, mock_stdout):
        with patch('builtins.input', return_value='rock'):
            with patch('random.choice', return_value='rock'):
                play_game()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You chose rock", output)
        self.assertIn("The computer chose rock", output)
        self.assertIn("It's a tie!", output)
        self.assertIn("Thanks for playing!", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_user_wins(self, mock_stdout):
        with patch('builtins.input', return_value='rock'):
            with patch('random.choice', return_value='scissors'):
                play_game()
        self.assertIn("You win!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_computer_wins(self, mock_stdout):
        with patch('builtins.input', return_value='rock'):
            with patch('random.choice', return_value='paper'):
                play_game()
        self.assertIn("The computer wins!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_valid_choice(self, mock_stdout):
        with patch('builtins.input', return_value='rock'):
            play_game()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You chose rock", output)
        self.assertIn("The computer chose", output)
        self.assertIn("Thanks for playing!", output)


if __name__ == '__main__':
    unittest.main()
