import unittest
from mock import MagicMock
from pytactoe.game import Game

class GameTests(unittest.TestCase):

    def test_game_initializes_with_a_fresh_board_by_default(self):
        spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        game = Game(None)

        self.assertEqual(spots, game.board.spots)

    def test_game_can_be_initialized_with_particular_board(self):
        spots = ["X", 2, "O", 4, 5, 6, 7, 8, 9]
        game = Game(None, None, None, spots)

        self.assertEqual(spots, game.board.spots)

class GamePlayersTests(unittest.TestCase):

    def setUp(self):
        self.player1 = MagicMock()
        self.player2 = MagicMock()
        self.game = Game(None, self.player1, self.player2)

    def test_game_initializes_with_two_players(self):
        self.assertEqual(self.game.player1, self.player1)

    def test_game_switches_players(self):
        self.assertEqual(self.player1, self.game.current_player)
        self.game.switch_players()
        self.assertEqual(self.player2, self.game.current_player)

    def test_retrieving_player_moves(self):
        self.player1.get_move = MagicMock(return_value=1)
        chosen_move = self.game.get_player_move()

        self.assertEqual(1, chosen_move)

    def test_placing_player_move(self):
        chosen_move = self.game.board.spots[0]
        self.game.place_move(chosen_move)

        self.assertEqual(self.player1.mark, self.game.board.spots[0])

class GameOverTests(unittest.TestCase):

    def setUp(self):
        self.player1 = MagicMock()
        self.player2 = MagicMock()
        self.mock_presenter = MagicMock()
        self.game = Game(self.mock_presenter, self.player1, self.player2)

        self.mock_presenter.stalemate_message = MagicMock()
        self.mock_presenter.winner_message = MagicMock()
        self.player1.mark = "X"

        self.stalemated_board =["X", "X", "O", "O", "O", "X", "X", "X", "O"]
        self.won_board = ["X", "X", "X", "O", "O", 6, 7, 8, 9]

    def test_game_is_over(self):
        self.assertFalse(self.game.is_over())

        self.game.board.spots = self.stalemated_board
        self.assertTrue(self.game.is_over())

        self.game.board.spots = self.won_board
        self.assertTrue(self.game.is_over())

    def test_game_over_presents_results(self):
        self.game.board.spots = self.stalemated_board
        self.game.is_over()
        self.mock_presenter.stalemate_message.assert_called_with()

        self.game.board.spots = self.won_board
        self.game.is_over()
        self.mock_presenter.winner_message.assert_called_with("X")
