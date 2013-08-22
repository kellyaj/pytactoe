import unittest
from mock import MagicMock
from pytactoe.board import Board
from pytactoe.computer import Computer

class ComputerTests(unittest.TestCase):

    def setUp(self):
        self.computer = Computer("O")
        self.board = Board()
        self.mock_presenter = MagicMock()
        self.mock_presenter.computer_move_message = MagicMock()

    def test_computer_initializes_with_a_mark(self):
        self.assertEqual("O", self.computer.mark)

    def test_computer_chooses_moves_from_available_spots(self):
        self.board.spots =[1, "X", "X", "O", "X", "O", "O", "O", "X"]
        available_spots = self.board.available_spots()
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertTrue(chosen_move in self.board.spots)

    def test_computer_chooses_obvious_win(self):
        self.board.spots =[1, "X", "X", "O", "X", "O", "O", "O", "X"]
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertEqual(1, chosen_move)

    def test_computer_chooses_winning_row_move(self):
        self.board.spots = ["X", "X", 3, 4, "X", 6, 7, "O", "O"]
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertEqual(7, chosen_move)

    def test_computer_chooses_winning_column_move(self):
        self.board.spots = ["X", 2, "O", "X", "O", 6, 7, 8, 9]
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertEqual(7, chosen_move)

    def test_computer_chooses_winning_diagonal_move(self):
        self.board.spots = [1, 2, "X", 4, "X", "O", "O", "O", "X"]
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertEqual(1, chosen_move)

    def test_computer_takes_win_over_block(self):
        self.board.spots = ["X", "X", 3, 4, "X", 6, "O", "O", 9]
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertEqual(9, chosen_move)

    def test_computer_takes_win_over_fork(self):
        self.board.spots = ["X", 2, "X", "O", "O", 6, "X", 8, 9]
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertEqual(6, chosen_move)
