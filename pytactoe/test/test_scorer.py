import unittest
from pytactoe.scorer import Scorer
from pytactoe.board import Board

class BoardEvaluationTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_evaluating_rows_as_wins(self):
        unwinning_row = ["X", 2, "O"]
        winning_row = ["X", "X", "X"]

        self.assertFalse(Scorer.row_won(unwinning_row))
        self.assertTrue(Scorer.row_won(winning_row))

    def test_evaluating_a_fresh_board(self):
        self.assertFalse(Scorer.is_game_won(self.board))

    def test_evaluating_an_in_progress_unwon_board(self):
        self.board.spots = ["X", "X", 3, "O", 5, 6, 7, 8, 9]
        self.assertFalse(Scorer.is_game_won(self.board))

    def test_evaluating_a_won_board(self):
        self.board.spots = ["X", "X", "X", "O", "O", 6, 7, 8, 9]
        self.assertTrue(Scorer.is_game_won(self.board))

    def test_checking_an_unstalemated_board(self):
        self.assertFalse(Scorer.is_game_stalemate(self.board))

    def test_checking_a_stalemated_board(self):
        self.board.spots = ["X", "X", "O", "O", "O", "X", "X", "X", "O"]
        self.assertTrue(Scorer.is_game_stalemate(self.board))

class GameOverTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_a_game_is_not_over_for_unwon_board(self):
        self.assertFalse(Scorer.is_game_over(self.board))

    def test_game_is_over_for_stalemated_board(self):
        self.board.spots = ["X", "X", "O", "O", "O", "X", "X", "X", "O"]
        self.assertTrue(Scorer.is_game_over(self.board))

    def test_game_is_over_for_a_won_board(self):
        self.board.spots = ["X", "X", "X", "O", "O", 6, 7, 8, 9]
        self.assertTrue(Scorer.is_game_over(self.board))
