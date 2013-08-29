class Human(object):

    def __init__(self, mark, io):
        self.mark = mark
        self.io = io

    def sanitize_user_input(self, user_input):
        try:
            sanitized_input = int(user_input)
        except TypeError:
            sanitized_input = 0
        except ValueError:
            sanitized_input = 0
        return sanitized_input

    def get_sanitized_input(self):
        user_input = self.io.get_input()
        return self.sanitize_user_input(user_input)

    def is_move_valid(self, move, board):
        return isinstance(move, int) and board.is_spot_available(move)

    def get_move(self, presenter, board):
        while 1:
            presenter.move_prompt(self.mark)
            presenter.available_moves_message(board.available_spots())
            chosen_move = self.get_sanitized_input()
            if self.is_move_valid(chosen_move, board):
                return chosen_move
            presenter.invalid_move_message()
