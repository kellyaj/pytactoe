from pytactoe.board import Board

class Game(object):

    def __init__(self, player1=None, player2=None, spots=None):
        self.board = Board(spots)
        self.player1 = player1
        self.player2 = player2
        self.players = [player1, player2]
        self.current_player = self.players[0]

    def switch_players(self):
        self.players.reverse()
        self.current_player = self.players[0]

    def get_player_move(self):
        selected_move = self.current_player.get_move(self.board.spots)
        if self.is_move_valid(selected_move):
            return selected_move
        else:
            self.get_player_move()

    def is_move_valid(self, move):
        return isinstance(move, int) and self.board.is_spot_available(move)

    def place_move(self, move):
        self.board.place_move(self.current_player.mark, move)
