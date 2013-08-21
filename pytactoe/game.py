import sys
from pytactoe.io import InputOutput
from pytactoe.board import Board
from pytactoe.presenter import Presenter

class Game(object):

    def __init__(self, io=None, player1=None, player2=None, spots=None):
        self.io = io or InputOutput(sys.stdout, sys.stdin)
        self.presenter = Presenter(io)
        self.board = Board(spots)
        self.player1 = player1
        self.player2 = player2
        self.players = [player1, player2]
        self.current_player = self.players[0]

    def switch_players(self):
        self.players.reverse()
        self.current_player = self.players[0]

    def get_player_move(self):
        return self.current_player.get_move(self.board.spots)

    def is_move_valid(self, move):
        return isinstance(move, int) and self.board.is_spot_available(move)
