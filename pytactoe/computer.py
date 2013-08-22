from player import Player
from scorer import Scorer

class Computer(Player):

    def __init__(self, mark):
        super(Computer, self).__init__(mark)

    def get_move(self, presenter, board):
        presenter.computer_move_message()
        self.current_player = self.mark
        chosen_move = self.minimax(board, self.current_player, 1)[1]
        return chosen_move

    def score_move(self, board, current_player, depth):
        if Scorer.is_game_won(board):
            return (1.0 / -depth)
        else:
            return 0

    def switch_players(self, current_player):
        if current_player == "X":
            return "O"
        else:
            return "X"

    def minimax(self, board, current_player, depth=0):
        spot_score = -1
        prime_move = 0
        highest_score = -1
        depth = depth
        if Scorer.is_game_over(board):
            return [self.score_move(board, current_player, depth), None]
        depth += 1
        for spot in board.available_spots():
            board.place_move(current_player, spot)
            spot_score = -(self.minimax(board, self.switch_players(current_player), depth)[0])
            board.spots[spot - 1] = spot
            if spot_score > highest_score:
                prime_move = spot
                highest_score = spot_score
        return [highest_score, prime_move]
