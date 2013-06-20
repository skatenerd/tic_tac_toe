import unittest
from ai import AI
from humanoid import Humanoid
from board import Board
from test_utils import MockUserInput

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
                           
