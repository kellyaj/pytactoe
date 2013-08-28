class Human(object):

    def __init__(self, mark, io):
        self.mark = mark
        self.io = io

    def get_move(self, presenter, board):
        presenter.move_prompt(self.mark)
        presenter.available_moves_message(board.available_spots())
        return self.io.get_input()
