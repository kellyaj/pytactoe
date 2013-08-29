import unittest
from mock import MagicMock
from pytactoe.human import Human

class HumanTests(unittest.TestCase):

    def setUp(self):
        self.mockio = MagicMock()
        self.mockio.get_input = MagicMock(return_value=1)
        self.human = Human("X", self.mockio)
        self.board = MagicMock()

    def test_human_initializes_with_a_mark(self):
        self.assertEqual(self.human.mark, "X")

    def test_human_initializes_with_io(self):
        self.assertEqual(self.human.io, self.mockio)

    def test_sanitizing_user_input(self):
        self.assertEqual(0, self.human.sanitize_user_input(None))
        self.assertEqual(0, self.human.sanitize_user_input(''))
        self.assertEqual(4, self.human.sanitize_user_input('4'))

    def test_getting_sanitized_move_from_human_player(self):
        self.assertEqual(1, self.human.get_sanitized_input())

    def test_retrieving_a_move_from_human_player(self):
        mock_presenter = MagicMock()
        chosen_move = self.human.get_move(mock_presenter, self.board)

        self.assertEqual(1, chosen_move)

    def test_validating_a_None_response(self):
        self.assertFalse(self.human.is_move_valid(None, self.board))

    def test_validating_a_taken_spot_response(self):
        self.board.is_spot_available = MagicMock(return_value=False)
        taken_spot = 5

        self.assertFalse(self.human.is_move_valid(taken_spot, self.board))

    def test_validating_an_non_integer_string_response(self):
        invalid_move = "banana"

        self.assertFalse(self.human.is_move_valid(invalid_move, self.board))

    def test_validating_a_proper_response(self):
        valid_move = 2

        self.assertTrue(self.human.is_move_valid(valid_move, self.board))
