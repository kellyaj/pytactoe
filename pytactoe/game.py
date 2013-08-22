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

    def sanitize_user_input(self, user_input):
        try:
            sanitized_input = int(user_input)
        except TypeError:
            sanitized_input = 0
        except ValueError:
            sanitized_input = 0
        return sanitized_input

    def get_player_move(self):
        while 1:
            selected_move = self.current_player.get_move(self.presenter, self.board)
            sanitized_input = self.sanitize_user_input(selected_move)
            if self.is_move_valid(sanitized_input):
                return sanitized_input
            self.presenter.invalid_move_message()

    def is_move_valid(self, move):
        return isinstance(move, int) and self.board.is_spot_available(move)

    def place_move(self, chosen_move):
        self.board.place_move(self.current_player.mark, chosen_move)

    def is_over(self):
        if Scorer.is_game_won(self.board):
            self.presenter.winner_message(self.current_player.mark)
        elif Scorer.is_game_stalemate(self.board):
            self.presenter.stalemate_message()
        return Scorer.is_game_over(self.board)
