import unittest
from mock import MagicMock
from pytactoe.human import Human

class HumanTests(unittest.TestCase):

  def setUp(self):
      self.mockio = MagicMock()
      self.mockio.get_input = MagicMock(return_value=1)
      self.mockio.move_prompt = MagicMock()
      self.human = Human("X", self.mockio)

  def test_human_initializes_with_a_mark(self):
      self.assertEqual(self.human.mark, "X")

  def test_retrieving_a_move_from_human_player(self):
      mock_board = MagicMock()
      mock_board.available_spots = MagicMock()
      chosen_move = self.human.get_move(self.mockio, mock_board)

      self.assertEqual(1, chosen_move)
