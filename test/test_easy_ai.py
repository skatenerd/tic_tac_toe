import unittest
from easy_ai import EasyAI
from board import Board
class AiDifficultyTests(unittest.TestCase):

    def test_easy_ai_returns_only_non_winning_moves(self):
        computer = EasyAI("o")
        board = Board()
        board.make_move(1,"o")
        board.make_move(5,"x")
        board.make_move(2,"o")
        board.make_move(6,"x")
        for i in range(100):
            self.assertTrue(computer.next_move(board) != 3)

    def test_easy_ai_has_token(self):
        computer = EasyAI("o")
        self.assertEqual("o",computer.token)