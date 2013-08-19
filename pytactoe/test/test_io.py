import unittest
import sys
import mock
from pytactoe.io import InputOutput
from cStringIO import StringIO

class InputOutputTests(unittest.TestCase):

    def test_printing(self):
        chosen_out = StringIO()
        chosen_in = StringIO()
        io = InputOutput(chosen_out, chosen_in)
        io.present("hello world")
        output = chosen_out.getvalue()
        self.assertEqual(output, "hello world\n")

    def test_getting_input(self):
        chosen_out = StringIO()
        chosen_in = StringIO("hello\n")
        io = InputOutput(chosen_out, chosen_in)
        given_input = io.get_input()
        self.assertEqual(given_input, "hello\n")
