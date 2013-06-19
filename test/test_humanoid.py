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

    def test_third_move_is_human(self):
        mock = MockUserInput([1,2,3])
        player = Humanoid("x",input_object=mock)
        board = Board()
        self.assertEqual(1,player.next_move(board))
        self.assertEqual(2,player.next_move(board))
        self.assertEqual(3,player.next_move(board))

    def test_that_fourth_move_is_ai(self):
        mock = MockUserInput([1,2,5])
        player = Humanoid("x",input_object=mock)
        board = Board()
        board.make_move(4,"o")
        board.make_move(8,"o") 
        for i in range(3):
            player.next_move(board)
        WINNERS = (3,9) 
        self.assertTrue(player.next_move(board) in WINNERS) 
