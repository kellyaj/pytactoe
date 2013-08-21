import unittest
from mock import MagicMock
from pytactoe.human import Human

class HumanTests(unittest.TestCase):

  def test_human_initializes_with_a_mark(self):
      human = Human("X", None)

      self.assertEqual(human.mark, "X")

  def test_retrieving_a_move_from_human_player(self):
      mockio = MagicMock()
      mockio.get_input = MagicMock(return_value=1)
      mockio.move_prompt = MagicMock()
      human = Human("X", mockio)
      chosen_move = human.get_move(mockio, None)

      self.assertEqual(1, chosen_move)
