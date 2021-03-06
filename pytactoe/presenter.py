class Presenter(object):

    def __init__(self, io):
        self.io = io

    def welcome_message(self):
        self.io.present("Welcome to Tic Tac Toe\n")

    def move_prompt(self, mark):
        self.io.present("%s, please select a move:\n" % mark)

    def play_again_prompt(self):
        self.io.present("Would you like to play again? type 'yes' or 'no'")

    def player_type_prompt(self, player_turn):
        self.io.present("The %s player is a... type 'human' or 'computer'" % player_turn)

    def available_moves_message(self, available_moves):
        self.io.present("Available moves: %s\n\n" % available_moves)

    def winner_message(self, mark):
        self.io.present("%s has won the game!\n" % mark)

    def invalid_move_message(self):
        self.io.present("Invalid move. Please try again")

    def stalemate_message(self):
        self.io.present("The game ended in a stalemate\n")

    def computer_move_message(self):
        self.io.present("Computer is thinking...\n")

