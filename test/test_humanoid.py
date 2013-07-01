import unittest
from humanoid import Humanoid
from board import Board
from test_utils import MockUserInput,FakePrinter

class HumanoidNextMoveTests(unittest.TestCase):

    def test_first_move_is_human(self):
        mock = MockUserInput([1])      
        player = Humanoid("x",input_object=mock)
        board = Board()
        self.assertEqual(1,player.next_move(board))
       
    def test_second_move_is_human(self):
        mock = MockUserInput([1,2])
        player = Humanoid("x",input_object=mock)
        board = Board()
        self.assertEqual(1,player.next_move(board))
        self.assertEqual(2,player.next_move(board))

    def test_third_move_is_ai(self):
        mock = MockUserInput([1,7])
        player = Humanoid("x",input_object=mock)
        board = Board()
        board.make_move(4,"o")
        board.make_move(5,"o") 
        self.assertEqual(1,player.next_move(board))
        board.make_move(1,"x") 
        self.assertEqual(7,player.next_move(board))
        board.make_move(7,"x") 
        self.assertEqual(6,player.next_move(board))
                         
    def test_for_prompts(self):
	mock = MockUserInput([1])
	fake_printer = FakePrinter()
	humanoid = Humanoid("x",mock,fake_printer)
	humanoid.next_move(Board())
	NOT_FOUND = -1
	history = "".join(fake_printer.history)
	status = history.find(humanoid.token.capitalize() + "'s turn")
	self.assertNotEqual(NOT_FOUND,status)
        
	status = history.find(humanoid.token.capitalize() + " moves to 1")
	self.assertNotEqual(NOT_FOUND,status)

	status = history.find("Available moves are " + str(Board().available_moves()))
	self.assertNotEqual(NOT_FOUND,status)

	status = history.find("Please select a move: ")
	self.assertNotEqual(NOT_FOUND,status)

    def test_that_input_prompts_arent_shown_to_humanoid_ai(self):
	fake_printer = FakePrinter()
	humanoid = Humanoid("x",fake_printer)
        humanoid.times_next_move_called = 3
	humanoid.next_move(Board())
	NOT_FOUND = -1
	status = self.build_and_search_history_string(fake_printer,"Available moves are")
	self.assertTrue(status == NOT_FOUND)

	status = self.build_and_search_history_string(fake_printer,"Please select a move: ")
	self.assertTrue(status == NOT_FOUND)

    def build_and_search_history_string(self,printer,search_string):
        history_string = "".join(printer.history)
	status = history_string.find(search_string)
	return status

