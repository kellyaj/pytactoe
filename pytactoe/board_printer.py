class BoardPrinter(object):

    def __init__(self, io):
        self.io = io

    def print_board(self, board):
        stringified_board = map(str, board)
        self.io.present("     " + ("   |   ").join(stringified_board[0:3]))
        self.io.present("    -------------------")
        self.io.present("     " + ("   |   ").join(stringified_board[3:6]))
        self.io.present("    -------------------")
        self.io.present("     " + ("   |   ").join(stringified_board[6:9]))
