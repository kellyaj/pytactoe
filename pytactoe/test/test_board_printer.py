import unittest
from cStringIO import StringIO
from pytactoe.board_printer import BoardPrinter
from pytactoe.io import InputOutput

class BoardPrinterTests(unittest.TestCase):

    def setUp(self):
        self.chosen_out = StringIO()
        self.io = InputOutput(StringIO, self.chosen_out)

    def test_printing_fresh_board(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        BoardPrinter.print_board(self.io, board)
        printed_board = ("     1   |   2   |   3\n"
                         "    -------------------\n"
                         "     4   |   5   |   6\n"
                         "    -------------------\n"
                         "     7   |   8   |   9\n\n\n")
        printed = self.chosen_out.getvalue()

        self.assertEqual(printed_board, printed)

    def test_printing_marked_board(self):
        board = ["X", 2, 3, 4, "O", 6, 7, 8, 9]
        BoardPrinter.print_board(self.io, board)
        printed_board = ("     X   |   2   |   3\n"
                         "    -------------------\n"
                         "     4   |   O   |   6\n"
                         "    -------------------\n"
                         "     7   |   8   |   9\n\n\n")
        printed = self.chosen_out.getvalue()

        self.assertEqual(printed_board, printed)
