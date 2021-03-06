import unittest
from pytactoe.board import Board

class BoardTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.default_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_board_initializes_with_spots(self):
        self.assertEqual(self.default_spots, self.board.spots)

    def test_board_can_have_spots_injected(self):
        spots_to_inject = ["X", 2, "O", 4, 5, 6, 7, 8, 9]
        board = Board(spots_to_inject)

        self.assertEqual(spots_to_inject, board.spots)

    def test_available_spots_list(self):
        self.assertEqual(self.default_spots, self.board.available_spots())

        self.board.place_move("X", 5)
        available_spots = [1, 2, 3, 4, 6, 7, 8, 9]

        self.assertEqual(available_spots, self.board.available_spots())

class BoardMovementTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_placing_moves_on_board(self):
        self.board.place_move("X",1)

        self.assertEqual("X", self.board.spots[0])

    def test_check_if_spot_is_available(self):
        self.board.place_move("O", 5)

        self.assertTrue(self.board.is_spot_available(1))
        self.assertFalse(self.board.is_spot_available(5))

class BoardRowRetrievalTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_getting_all_horizontal_rows(self):
        expected_rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.assertEqual(expected_rows, self.board.horizontal_rows())

    def test_getting_all_vertical_rows(self):
        expected_rows = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

        self.assertEqual(expected_rows, self.board.vertical_rows())

    def test_getting_all_diagonal_rows(self):
        expected_rows = [[1, 5, 9], [3, 5, 7]]

        self.assertEqual(expected_rows, self.board.diagonal_rows())

    def test_getting_all_rows_columns_and_diagonals(self):
        expected_rows = [
                          [1, 2, 3], [4, 5, 6], [7, 8, 9],
                          [1, 4, 7], [2, 5, 8], [3, 6, 9],
                          [1, 5, 9], [3, 5, 7]
                        ]

        self.assertEqual(expected_rows, self.board.get_all_rows())
