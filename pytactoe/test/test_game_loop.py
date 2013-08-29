import unittest
from mock import MagicMock
from cStringIO import StringIO
from pytactoe.game_loop import GameLoop
from pytactoe.human import Human
from pytactoe.computer import Computer
from pytactoe.io import InputOutput

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

    def test_game_is_created_with_proper_player_types(self):
        io = InputOutput(StringIO("human\ncomputer"), StringIO())
        game_loop = GameLoop(io)

        self.assertTrue(isinstance(game_loop.game.player1, Human))
        self.assertTrue(isinstance(game_loop.game.player2, Computer))

    def test_evaluting_yes_response_to_play_again_prompt(self):
        io = InputOutput(StringIO("c\nc\nyes\n"), StringIO())
        game_loop = GameLoop(io)
        game_loop.create_game(self.player1, self.player2)
        self.assertTrue(game_loop.play_again())

    def test_evaluting_no_response_to_play_again_prompt(self):
        io = InputOutput(StringIO("c\nc\nno\n"), StringIO())
        game_loop = GameLoop(io)
        game_loop.create_game(self.player1, self.player2)
        self.assertFalse(game_loop.play_again())
