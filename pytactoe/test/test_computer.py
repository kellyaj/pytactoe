import unittest
from pytactoe.computer import Computer

class ComputerTests(unittest.TestCase):

    def setUp(self):
        self.computer = Computer("O")
        self.available_spots = [2, 3, 4, 5, 6, 7, 8, 9]

    def test_computer_initializes_with_a_mark(self):
        self.assertEqual("O", self.computer.mark)

    def test_computer_chooses_integers(self):
        chosen_move = self.computer.get_move(self.available_spots)

        self.assertTrue(isinstance(chosen_move, int))

    def test_computer_chooses_moves_from_available_spots(self):
        chosen_move = self.computer.get_move(self.available_spots)

        self.assertTrue(chosen_move in self.available_spots)
