import unittest
from pytactoe.scorer import Scorer

class ScorerTests(unittest.TestCase):

    def test_evaluating_rows_as_wins(self):
        unwinning_row = ["X", 2, "O"]
        winning_row = ["X", "X", "X"]
        self.assertFalse(Scorer.row_won(unwinning_row))
        self.assertTrue(Scorer.row_won(winning_row))

