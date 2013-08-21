import unittest
from pytactoe.human import Human

class HumanTests(unittest.TestCase):

  def test_human_initializes_with_a_mark(self):
      human = Human("X")

      self.assertEqual(human.mark, "X")
