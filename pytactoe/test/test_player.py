import unittest
from pytactoe.player import Player

class PlayerTests(unittest.TestCase):

  def test_player_initializes_with_a_mark(self):
      player = Player("X")

      self.assertEqual(player.mark, "X")
