from player import Player

class Human(Player):

    def __init__(self, mark, io):
        super(Human, self).__init__(mark)
        self.io = io

    def get_move(self, presenter, board):
        presenter.move_prompt(self.mark)
        presenter.available_moves_message(board.available_spots())
        return self.io.get_input()
