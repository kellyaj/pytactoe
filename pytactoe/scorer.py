class Scorer(object):

    @staticmethod
    def row_won(row):
        return len(row) != len(set(row))
