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
