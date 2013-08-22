import unittest
from mock import MagicMock
from pytactoe.game_loop import GameLoop
from pytactoe.io import InputOutput
from cStringIO import StringIO

class GameLoopTests(unittest.TestCase):

    def setUp(self):
        self.player1 = MagicMock()
        self.player2 = MagicMock()

    def test_game_is_created_with_correct_players(self):
        io = InputOutput(StringIO(), StringIO())
        game_loop = GameLoop(io)
        game_loop.create_game(self.player1, self.player2)

        self.assertEqual(self.player1, game_loop.game.player1)
        self.assertEqual(self.player2, game_loop.game.player2)

    def test_evaluting_play_again_prompt(self):
        io = InputOutput(StringIO(), StringIO("c\nc\nyes\n"))
        game_loop = GameLoop(io)
        game_loop.create_game(self.player1, self.player2)
        self.assertTrue(game_loop.play_again())
