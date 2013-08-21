import unittest
from pytactoe.computer import Computer

class ComputerTests(unittest.TestCase):

    def test_computer_initializes_with_a_mark(self):
        computer = Computer("O")

        self.assertEqual("O", computer.mark)
