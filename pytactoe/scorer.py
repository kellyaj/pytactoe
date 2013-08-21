class Scorer(object):

    @staticmethod
    def row_won(row):
        return row[0] == row[1] == row[2]

    @staticmethod
    def is_game_won(board):
        for row in board.get_all_rows():
            if True in map(lambda x: Scorer.row_won(x), board.get_all_rows()):
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
        board_as_string = map(lambda x: Scorer.convert_int_or_zero(x), board.spots)
        return sum(board_as_string) == 0

    @staticmethod
    def is_game_over(board):
        return Scorer.is_game_won(board) | Scorer.is_game_stalemate(board)
