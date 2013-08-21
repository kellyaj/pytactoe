class BoardPrinter(object):

    @staticmethod
    def print_board(io, board):
        stringified_board = map(str, board)
        io.present("     " + ("   |   ").join(stringified_board[0:3]))
        io.present("    -------------------")
        io.present("     " + ("   |   ").join(stringified_board[3:6]))
        io.present("    -------------------")
        io.present("     " + ("   |   ").join(stringified_board[6:9]))
