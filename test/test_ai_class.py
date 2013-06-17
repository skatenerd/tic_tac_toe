import sys
import unittest
sys.path.append("../")
from ai import *
from board import *
from player import *
from easy_ai import EasyAI

class AiNextMoveTests(unittest.TestCase):

    def test_if_ai_blocks_potential_win(self):
          computer = AI('x')
          game_board = Board()
          game_board.make_move(1,'o')
          game_board.make_move(5,'x')
          game_board.make_move(3,'o')
          computer_move = computer.next_move(game_board)
          self.assertEqual(2,computer_move)

    def test_if_ai_blocks_diagonal_win(self):
          game_board = Board()
          computer = AI('x')
          game_board.make_move(1,'o')
          game_board.make_move(5,'o')
          game_board.make_move(3,'x')
          computer_move = computer.next_move(game_board)
          self.assertEqual(9,computer_move)

    def test_if_ai_chooses_corner(self):
          computer = AI('o')
          game_board = Board()
          actual_move = computer.next_move(game_board)
          corners = (1,3,5,7,9)
          self.assertTrue(actual_move in corners)

    def test_if_ai_chooses_winning_move_with_threat(self):
          computer = AI('o')
          game_board = Board()
          game_board.make_move(1,'o')
          game_board.make_move(4,'x')
          game_board.make_move(5,'x')
          game_board.make_move(2,'o')
          computer_move = computer.next_move(game_board)
          self.assertEqual(3,computer_move)

    def test_if_ai_stops_three_way_setup(self):
          computer = AI('o')
          game_board = Board()
          game_board.make_move(1,'x')
          computer_move = computer.next_move(game_board)
          self.assertEqual(True,computer_move in (2,5))

    def test_ai_move_defense(self):
        board = Board()
        computer = AI("o")
        board.make_move(1,'o')
        board.make_move(5,'x')
        board.make_move(9,'x')
        move = computer.next_move(board)
        self.assertTrue(move in (3,7))

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

        
