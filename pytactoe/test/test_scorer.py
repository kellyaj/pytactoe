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

    def test_handling_valueerror_for_player_marks(self):
        my_int = 4
        my_string = "four"

        self.assertEqual(4, Scorer.convert_int_or_zero(my_int))
        self.assertEqual(0, Scorer.convert_int_or_zero(my_string))

    def test_checking_for_stalemate(self):
        fresh_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        stalemated_board =["X", "X", "O", "O", "O", "X", "X", "X", "O"]

        self.assertFalse(Scorer.is_game_stalemate(fresh_board))
        self.assertTrue(Scorer.is_game_stalemate(stalemated_board))
