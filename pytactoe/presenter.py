class Presenter(object):

    def __init__(self, io):
        self.io = io

    def welcome_message(self):
        self.io.present("Welcome to Tic Tac Toe")

    def move_prompt(self, mark):
        self.io.present("%s, please select a move:" % mark)

    def player_type_prompt(self, player_turn):
        self.io.present("The %s player is a... type 'human' or 'computer'" % player_turn)

    def winner_message(self, mark):
        self.io.present("%s has won the game!" % mark)

    def invalid_move_message(self):
        self.io.present("Invalid move. Please try again")

    def stalemate_message(self):
        self.io.present("The game ended in a stalemate")
