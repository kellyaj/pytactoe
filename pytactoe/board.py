class Board(object):

    def __init__(self, size):
        self.spots = ["" for n in range(size)]

    def place_move(self, mark, spot):
        self.spots[spot - 1] = mark

    def spot_is_taken(self, spot):
        return self.spots[spot - 1] != ""

    def available_spots(self):
        available_spots = []
        for idx, val in enumerate(self.spots):
            if val == "":
                available_spots.append(idx + 1)
        return available_spots
