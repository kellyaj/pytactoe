import unittest
import sys
import mock
from pytactoe.io import InputOutput
from cStringIO import StringIO

class InputOutputTests(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_printing(self):
        io = InputOutput(sys.stdout, sys.stdin)
        io.present("hello world")
        self.assertEqual(sys.stdout.getvalue(), "hello world\n")

    def test_getting_input(self):
        io = InputOutput(sys.stdout, sys.stdin)
        with mock.patch('__builtin__.raw_input', return_value = "hello"):
            assert io.get_input() == "hello"
