import sys
from io import InputOutput
from game import Game
from presenter import Presenter
from board_printer import BoardPrinter
from human import Human
from computer import Computer

class GameLoop(object):

    def __init__(self, io):
        self.io = io or InputOutput(sys.stdout, sys.stdin)
        self.presenter = Presenter(io)
        self.create_players(self.choose_player_type("first"), self.choose_player_type("second"))
        self.create_game(self.player1, self.player2)

    def run(self, game):
        self.presenter.welcome_message()
        while game.is_over() == False:
            BoardPrinter.print_board(self.io, game.board.spots)
            game.place_move(game.get_player_move())
            if game.is_over():
                BoardPrinter.print_board(self.io, game.board.spots)
                break
            game.switch_players()

    def start_game(self):
        self.run(self.game)

    def create_game(self, player1, player2):
        self.game = Game(self.presenter, player1, player2)

    def choose_player_type(self, player_turn):
        self.presenter.player_type_prompt(player_turn)
        return self.io.get_input()

    def create_players(self, player1_response, player2_response):
        player1 = player1_response.rstrip().lower()
        player2 = player2_response.rstrip().lower()
        if player1 == "human":
            self.player1 = Human("X", self.io)
        else:
            self.player1 = Computer("X")
        if player2 == "human":
            self.player2 = Human("O", self.io)
        else:
            self.player2 = Computer("O")
