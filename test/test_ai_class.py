import sys
import unittest
sys.path.append("../")
from ai import *
from board import *
from player import *

class AiInitTests(unittest.TestCase):

    def test_if_init_function_sets_token(self):
          computer = AI('x')
          self.assertEqual('x',computer.token)

    def test_if_init_function_sets_opp_token(self):
          computer = AI('x')
          self.assertEqual('o', computer.opponent_token)

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

    def test_ai_vs_ai(self):
          computer_x = AI('x')
          computer_o = AI('o')
          game_board = Board()
          for i in range(6):
              x = computer_x.next_move(game_board)
              game_board.make_move(x,computer_x.token)
              o = computer_o.next_move(game_board)
              game_board.make_move(o,computer_o.token)
          self.assertEqual(None,game_board.winner())

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

class AiBestMoveScoreTests(unittest.TestCase):

    def test_if_best_moves_returns_neg_one_first_turn(self):
          computer = AI('o')
          game = Board()
          neutral_score = 0
          generated_score = computer.best_score(1,game,'o')
          self.assertEqual(neutral_score,generated_score)


    def test_if_returns_neg_one_when_opp_wins(self):
          computer = AI('o')
          game_board = Board()
          game_board.make_move(1,'x')
          game_board.make_move(2,'x')
          game_board.make_move(3,'x')
          bad_score = -1
          generated_score = computer.best_score(4,game_board,'o')
          self.assertEqual(bad_score,generated_score)

    def test_if_returns_one_when_self_wins(self):
          computer = AI('o')
          game_board = Board()
          game_board.make_move(1,'o')
          game_board.make_move(2,'o')
          good_score = 1
          generated_score = computer.best_score(3, game_board, 'o')
          self.assertEqual(good_score,generated_score)

    def test_if_returns_one_when_self_wins_with_x_token(self):
          computer = AI('x')
          game_board = Board()
          game_board.make_move(1,'x')
          game_board.make_move(2,'x')
          game_board.make_move(3,'x')
          good_score = 1
          generated_score = computer.best_score(4, game_board, 'x')
          self.assertEqual(good_score,generated_score)

class AICostFunctionTests(unittest.TestCase):

    def test_if_cost_function_returns_zero_with_no_winner(self):
          computer = AI('o')
          game_board = Board()
          cost = computer.cost_function(game_board.winner())
          self.assertEqual(0,cost)

    def test_if_cost_function_returns_one_with_ai_winner(self):
          computer = AI('o')
          game_board = Board()
          game_board.make_move(1,'o')
          game_board.make_move(2, 'o')
          game_board.make_move(3, 'o')
          cost = computer.cost_function(game_board.winner())
          self.assertEqual(1, cost)

    def test_if_cost_function_returns_neg_one_with_opp_winner(self):
          computer = AI('o')
          self.assertEqual(-1,computer.cost_function('x'))

    def test_cost_function_works_with_both_tokens(self):
          computer = AI('x')
          self.assertEqual(-1,computer.cost_function('o'))
