import unittest
from pytactoe.scorer import Scorer

class ScorerTests(unittest.TestCase):

    def test_evaluating_rows_as_wins(self):
        unwinning_row = ["X", 2, "O"]
        winning_row = ["X", "X", "X"]

        self.assertFalse(Scorer.row_won(unwinning_row))
        self.assertTrue(Scorer.row_won(winning_row))

    def test_evaluating_a_board_as_won(self):
        not_win_row = [1, 2, 3]
        win_row = ["X", "X", "X"]

        self.assertFalse(Scorer.is_game_won(not_win_row, not_win_row, not_win_row))
        self.assertTrue(Scorer.is_game_won(win_row, not_win_row, not_win_row))
        self.assertTrue(Scorer.is_game_won(not_win_row, win_row, not_win_row))
        self.assertTrue(Scorer.is_game_won(not_win_row, not_win_row, win_row))
