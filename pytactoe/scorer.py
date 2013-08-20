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
