import unittest
from mock import MagicMock
from pytactoe.game_loop import GameLoop
from pytactoe.io import InputOutput
from cStringIO import StringIO

class GameLoopTests(unittest.TestCase):

    def test_game_is_created_with_correct_players(self):
        player1 = MagicMock()
        player2 = MagicMock()
        io = InputOutput(StringIO(), StringIO())
        game_loop = GameLoop(io)
        game_loop.create_game(player1, player2)

        self.assertEqual(player1, game_loop.game.player1)
        self.assertEqual(player2, game_loop.game.player2)

    def test_evaluting_play_again_prompt(self):
        player1 = MagicMock()
        player2 = MagicMock()
        io = InputOutput(StringIO(), StringIO("c\nc\nyes\n"))
        game_loop = GameLoop(io)
        game_loop.create_game(player1, player2)
        self.assertTrue(game_loop.play_again())
