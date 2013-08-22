import unittest
from cStringIO import StringIO
from pytactoe.presenter import Presenter
from pytactoe.io import InputOutput

class PresenterTests(unittest.TestCase):

    def setUp(self):
        self.chosen_output = StringIO()
        self.io = InputOutput(self.chosen_output, None)
        self.presenter = Presenter(self.io)

    def test_presenting_the_welcome_message(self):
        expected_welcome = "Welcome to Tic Tac Toe\n"
        self.presenter.welcome_message()
        received_output = self.chosen_output.getvalue()

        self.assertEqual(received_output, expected_welcome)

    def test_presenting_the_move_prompt(self):
        expected_prompt = "X, please select a move:\n"
        self.presenter.move_prompt("X")
        received_output = self.chosen_output.getvalue()

    def test_presenting_the_player_type_prompt(self):
        expected_prompt = "The first player is a... type 'human' or 'computer'\n"
        self.presenter.player_type_prompt("first")
        received_output = self.chosen_output.getvalue()

        self.assertEqual(received_output, expected_prompt)

    def test_presenting_the_player_type_prompt(self):
        expected_prompt = "Would you like to play again? type 'yes' or 'no'\n"
        self.presenter.play_again_prompt()
        received_output = self.chosen_output.getvalue()

        self.assertEqual(received_output, expected_prompt)

    def test_presenting_the_winner_message(self):
        expected_winner_message = "O has won the game!\n"
        self.presenter.winner_message("O")
        received_output = self.chosen_output.getvalue()

        self.assertEqual(received_output, expected_winner_message)

    def test_presenting_invalid_move_message(self):
        expected_invalid_move_message = "Invalid move. Please try again\n"
        self.presenter.invalid_move_message()
        received_output = self.chosen_output.getvalue()

        self.assertEqual(received_output, expected_invalid_move_message)

    def test_presenting_stalemate_message(self):
        expected_stalemate_message = "The game ended in a stalemate\n"
        self.presenter.stalemate_message()
        received_output = self.chosen_output.getvalue()

        self.assertEqual(received_output, expected_stalemate_message)

    def test_presenting_stalemate_message(self):
        expected_computer_move_message = "Computer is thinking...\n"
        self.presenter.computer_move_message()
        received_output = self.chosen_output.getvalue()

        self.assertEqual(received_output, expected_computer_move_message)
