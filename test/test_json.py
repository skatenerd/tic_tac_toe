import unittest
from board import Board
import test_utils
from jsonify import *

class JsonPrinterTests(unittest.TestCase):

    def test_it_implements_display_method(self):
        printer = JsonPrinter()
        self.assertTrue("display" in dir(printer))

    def test_that_it_outputs_json_strings(self):
        printer = JsonPrinter()
        self.assertEqual(str,type(printer.display("string")))
 
    def test_that_it_outputs_json_hashes(self):
        printer = JsonPrinter()
        self.assertTrue(type(printer.display({"hash":"hashee"}) is type(dict)))

    def test_that_it_handles_board_output(self):
        printer = JsonPrinter()
        board = Board()
        board.make_move(1,"x")
       # self.assertEqual({"1":"x"},printer.display(board))
   
