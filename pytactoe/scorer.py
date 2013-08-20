class Scorer(object):

    @staticmethod
    def row_won(row):
        return len(row) != len(set(row))

    @staticmethod
    def is_game_won(rows, columns, diagonals):
        spaces = [rows, columns, diagonals]
        if True in map(lambda x: Scorer.row_won(x), spaces):
          return True
        else:
          return False

    @staticmethod
    def convert_int_or_zero(item):
        try:
            return int(item)
        except ValueError:
            return 0

    @staticmethod
    def is_game_stalemate(board):
        board_as_string = map(lambda x: Scorer.convert_int_or_zero(x), board)
        return sum(board_as_string) == 0
