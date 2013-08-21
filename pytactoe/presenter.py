class Presenter(object):

    def __init__(self, io):
        self.io = io

    def welcome_message(self):
        self.io.present("Welcome to Tic Tac Toe")

    def move_prompt(self, mark):
        self.io.present("%s, please select a move:" % mark)

    def winner_message(self, mark):
        self.io.present("%s has won the game!" % mark)

    def invalid_move_message(self):
        self.io.present("Invalid move. Please try again")
