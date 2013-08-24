import unittest
from mock import MagicMock
from pytactoe.board import Board
from pytactoe.computer import Computer

class ComputerTests(unittest.TestCase):

    def setUp(self):
        self.computer = Computer("O")
        self.board = Board()

    def test_computer_initializes_with_a_mark(self):
        self.assertEqual("O", self.computer.mark)

    def test_checking_first_move(self):
        self.assertTrue(self.computer.is_first_move(self.board))

        self.board.spots = [1, 2, 3, 4, "O", 6, 7, 8, 9]
        self.assertFalse(self.computer.is_first_move(self.board))

        self.board.spots =[1, "X", "X", "O", "X", "O", "O", "O", "X"]
        self.assertFalse(self.computer.is_first_move(self.board))

class ComputerMoveChoiceTests(unittest.TestCase):

    def setUp(self):
        self.computer = Computer("O")
        self.board = Board()
        self.mock_presenter = MagicMock()
        self.mock_presenter.computer_move_message = MagicMock()

    def test_computer_chooses_moves_from_available_spots(self):
        self.board.spots =[1, "X", "X", "O", "X", "O", "O", "O", "X"]
        available_spots = self.board.available_spots()
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertTrue(chosen_move in self.board.spots)

    def test_computer_choses_first_move_optimally(self):
        optimal_moves = [1, 3, 5, 7, 9]
        chosen_move = self.computer.get_move(self.mock_presenter, self.board)

        self.assertTrue(chosen_move in optimal_moves)

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

class ScoreMoveTests(unittest.TestCase):

    def setUp(self):
        self.computer = Computer("X")
        self.board = Board()
        self.winning_spots = ["X", "X", 3, 4, "X", 6, "O", "O", "O"]

    def test_stalemates_are_scored_as_zero(self):
        stalemated_board = ["X", "O", "O", "O", "X", "X", "X", "X", "O"]
        self.board.spots = stalemated_board
        score = self.computer.score_move(self.board, "X", 1)
        self.assertEqual(score, 0)

    def test_wins_are_score_as_one(self):
        self.board.spots = self.winning_spots
        score = self.computer.score_move(self.board, "X", 1)
        self.assertEqual(score, -1)

    def test_lower_depths_received_higher_scores(self):
        self.board.spots = self.winning_spots
        low_depth_score = -(self.computer.score_move(self.board, "X", 1))
        high_depth_score = -(self.computer.score_move(self.board, "X", 2))

        self.assertTrue(low_depth_score > high_depth_score)
