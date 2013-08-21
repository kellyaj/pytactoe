import unittest
from mock import MagicMock
from pytactoe.game import Game

class GameTests(unittest.TestCase):

    def test_game_initializes_with_a_fresh_board_by_default(self):
        spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        game = Game()

        self.assertEqual(spots, game.board.spots)

    def test_game_can_be_initialized_with_particular_board(self):
        spots = ["X", 2, "O", 4, 5, 6, 7, 8, 9]
        game = Game(None, None, None, spots)

        self.assertEqual(spots, game.board.spots)

    def test_game_initializes_with_two_players(self):
        player1 = MagicMock()
        player2 = MagicMock()
        game = Game(player1, player2)

        self.assertTrue(isinstance(game.player1, MagicMock))

    def test_game_switches_players(self):
        player1 = MagicMock()
        player2 = MagicMock()
        game = Game(None, player1, player2)

        self.assertEqual(player1, game.current_player)
        game.switch_players()
        self.assertEqual(player2, game.current_player)
