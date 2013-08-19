import unittest
from pytactoe.board import Board

class BoardTests(unittest.TestCase):

    def setUp(self):
        self.board = Board(9)

    def test_board_initializes_with_spots(self):
        self.assertEqual(["" for n in range(9)], self.board.spots)

    def test_placing_moves_on_board(self):
        self.board.place_move("X",1)
        self.assertEqual("X", self.board.spots[0])

    def test_spot_is_taken(self):
        self.board.place_move("O", 5)
        self.assertFalse(self.board.spot_is_taken(1))
        self.assertTrue(self.board.spot_is_taken(5))

    def test_available_spots_list(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], self.board.available_spots())
        self.board.place_move("X", 5)
        self.assertEqual([1, 2, 3, 4, 6, 7, 8, 9], self.board.available_spots())
