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
        game = Game(None, None, spots)

        self.assertEqual(spots, game.board.spots)

    def test_game_initializes_with_two_players(self):
        player1 = MagicMock()
        player2 = MagicMock()
        game = Game(player1, player2)

        self.assertTrue(isinstance(game.player1, MagicMock))

    def test_game_switches_players(self):
        player1 = MagicMock()
        player2 = MagicMock()
        game = Game(player1, player2)

        self.assertEqual(player1, game.current_player)
        game.switch_players()
        self.assertEqual(player2, game.current_player)

    def test_retrieving_player_moves(self):
        player1 = MagicMock()
        player1.get_move = MagicMock(return_value=1)
        game = Game(player1)
        chosen_move = game.get_player_move()

        self.assertEqual(1, chosen_move)

    def test_validating_player_move(self):
        spots = ["X", 2, "O", 4, 5, 6, 7, 8, 9]
        game = Game(None, None, spots)
        taken_spot = 1
        invalid_move = "banana"
        valid_move = 2

        self.assertFalse(game.is_move_valid(taken_spot))
        self.assertFalse(game.is_move_valid(invalid_move))
        self.assertTrue(game.is_move_valid(valid_move))

    def test_placing_player_move(self):
        player1 = MagicMock()
        player1.mark = "X"
        game = Game(player1)
        chosen_move = game.board.spots[0]
        game.place_move(chosen_move)

        self.assertEqual(player1.mark, game.board.spots[0])

    def test_game_is_over(self):
        game = Game()
        self.assertFalse(game.is_over())

        stalemated_board =["X", "X", "O", "O", "O", "X", "X", "X", "O"]
        game.board.spots = stalemated_board
        self.assertTrue(game.is_over())

        won_board = ["X", "X", "X", "O", "O", 6, 7, 8, 9]
        game.board.spots = won_board
        self.assertTrue(game.is_over())

