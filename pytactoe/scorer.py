class Scorer(object):

    @staticmethod
    def row_won(row):
        return len(row) != len(set(row))

    @staticmethod
    def is_game_won(all_rows):
        if True in map(lambda x: Scorer.row_won(x), all_rows):
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

    @staticmethod
    def is_game_over(board, all_rows):
        return Scorer.is_game_won(all_rows) | Scorer.is_game_stalemate(board)
