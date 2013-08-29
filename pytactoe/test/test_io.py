import unittest
from cStringIO import StringIO
from pytactoe.io import InputOutput

class InputOutputTests(unittest.TestCase):

    def test_printing(self):
        chosen_in = StringIO()
        chosen_out = StringIO()
        io = InputOutput(chosen_in, chosen_out)
        io.present("hello world")
        output = chosen_out.getvalue()

        self.assertEqual(output, "hello world\n")

    def test_getting_input(self):
        chosen_in = StringIO("hello\n")
        chosen_out = StringIO()
        io = InputOutput(chosen_in, chosen_out)
        given_input = io.get_input()

        self.assertEqual(given_input, "hello\n")
