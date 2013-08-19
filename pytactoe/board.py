class Board(object):

    def __init__(self):
        self.spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def place_move(self, mark, spot):
        self.spots[spot - 1] = mark

    def is_spot_taken(self, spot):
        return isinstance(self.spots[spot - 1], str)

    def available_spots(self):
        available_spots = []
        for idx, val in enumerate(self.spots):
            if isinstance(val, int):
                available_spots.append(idx + 1)
        return available_spots

    def get_all_rows(self):
        rows = []
        rows.append(self.spots[0:3])
        rows.append(self.spots[3:6])
        rows.append(self.spots[6:9])
        return rows

    def get_all_columns(self):
        columns = []
        columns.append([self.spots[i] for i in 0, 3, 6])
        columns.append([self.spots[i] for i in 1, 4, 7])
        columns.append([self.spots[i] for i in 2, 5, 8])
        return columns

    def get_all_diagonals(self):
        diagonals = []
        diagonals.append([self.spots[i] for i in 0, 4, 8])
        diagonals.append([self.spots[i] for i in 2, 4, 6])
        return diagonals

