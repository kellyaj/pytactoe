class Board(object):

    def __init__(self, spots=None):
        self.spots = spots or [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def place_move(self, mark, spot):
        self.spots[spot - 1] = mark

    def is_spot_available(self, spot):
        return spot in self.available_spots()

    def available_spots(self):
        available_spots = []
        for idx, val in enumerate(self.spots):
            if isinstance(val, int):
                available_spots.append(idx + 1)
        return available_spots

    def horizontal_rows(self):
        horizontal_rows = []
        horizontal_rows.append(self.spots[0:3])
        horizontal_rows.append(self.spots[3:6])
        horizontal_rows.append(self.spots[6:9])
        return horizontal_rows

    def vertical_rows(self):
        vertical_rows = []
        vertical_rows.append([self.spots[i] for i in 0, 3, 6])
        vertical_rows.append([self.spots[i] for i in 1, 4, 7])
        vertical_rows.append([self.spots[i] for i in 2, 5, 8])
        return vertical_rows

    def diagonal_rows(self):
        diagonal_rows = []
        diagonal_rows.append([self.spots[i] for i in 0, 4, 8])
        diagonal_rows.append([self.spots[i] for i in 2, 4, 6])
        return diagonal_rows

    def get_all_rows(self):
        horizontal = self.horizontal_rows()
        vertical = self.vertical_rows()
        diagonal = self.diagonal_rows()
        return horizontal + vertical + diagonal
