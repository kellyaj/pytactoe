from board import Board
from scorer import Scorer

class Game(object):

    def __init__(self, presenter, player1=None, player2=None, spots=None):
        self.presenter = presenter
        self.board = Board(spots)
        self.player1 = player1
        self.player2 = player2
        self.players = [player1, player2]
        self.current_player = self.players[0]

    def switch_players(self):
        self.players.reverse()
        self.current_player = self.players[0]

    def get_player_move(self):
        return self.current_player.get_move(self.presenter, self.board)

    def place_move(self, chosen_move):
        self.board.place_move(self.current_player.mark, chosen_move)

    def is_over(self):
        if Scorer.is_game_won(self.board):
            self.presenter.winner_message(self.current_player.mark)
        elif Scorer.is_game_stalemate(self.board):
            self.presenter.stalemate_message()
        return Scorer.is_game_over(self.board)
