#the test files are redundantly named, they could be called:
#board_test.py, game_test.py, etc.

import unittest
import sys
sys.path.append("../")
from board import *
from ai import *
from player import *

class BoardInitTests(unittest.TestCase):

    def test_if_new_board_is_empty_dict(self):
        self.assertEqual(dict(),Board().board_state)

class Board__Str__Tests(unittest.TestCase):

    def test_if_game_returns_no_pieces(self):
        game_board = Board()
        self.assertEqual(-1,game_board.__str__().find('x'))
        self.assertEqual(-1,game_board.__str__().find('o'))
        for num in range(1,10):
            self.assertEqual(-1,game_board.__str__().find(str(num)))

    def test_if_game_board_returns_correct_layout(self):
        game_board = Board()
        game_board.make_move(1,'x')
        #this might be a little clearer if you used "count" or something,
        #so I don't have to know what "-1" means
        self.assertNotEqual(-1,game_board.__str__().find('x'))

class BoardStateTests(unittest.TestCase):

    def test_if_state_returns_empty_dict_with_no_moves(self):
      board = Board()
      self.assertEqual(dict(),board.state())

    def test_if_state_returns_correct_mappings(self):
      board = Board()
      board.make_move(1,'x')
      board.make_move(3,'o')
      self.assertEqual({1:'x',3:'o'},board.state())

class BoardMakeMoveTests(unittest.TestCase):

    def test_if_make_move_alters_board_state(self):
        empty_board_state = Board()
        sample_board = Board()
        sample_board.make_move(1,'x')
        self.assertNotEqual(empty_board_state, sample_board.board_state)

class BoardGameOverTests(unittest.TestCase):

    def test_if_game_over_returns_false_at_game_beginning(self):
        game_board = Board()
        self.assertEqual(False, game_board.game_over())

    def test_if_game_over_returns_true_when_board_is_full(self):
        game_board = Board()
        for i in range(1,10):
            game_board.make_move(i,'x')
        self.assertEqual(True,game_board.game_over())

    def test_if_game_over_returns_true_when_there_is_winner(self):
        game_board = Board()
        for i in range(1,4):
            game_board.make_move(i,'x')
        self.assertEqual(True,game_board.game_over())

    def test_if_game_over_returns_false_with_empty_square(self):
        game_board = Board()
        for i in range(1,6):
          if i % 2 != 0:
            game_board.make_move(i,'x')
          else:
            game_board.make_move(i,'o')
        game_board.make_move(7,'o')
        game_board.make_move(8,'x')
        self.assertEqual(False,game_board.game_over())

    def test_if_game_over_returns_false_with_three_empty_squares(self):
        game_board = Board()
        game_board.make_move(1,'x')
        game_board.make_move(2,'o')
        game_board.make_move(3,'x')
        game_board.make_move(4,'o')
        game_board.make_move(5,'x')
        game_board.make_move(6,'o')
        self.assertEqual(False,game_board.game_over())

class BoardWinnerTests(unittest.TestCase):

    #these tests could be a lot less verbose:
    # def winner_returns_none_with_blank_board(), etc.
    def test_if_winner_returns_none_with_blank_board(self):
        self.assertEqual(None,Board().winner())

    def test_if_winner_returns_none_with_no_win(self):
        game_board = Board()
        game_board.make_move(1,'x')
        self.assertEqual(None,game_board.winner())

    def test_if_winner_returns_token_with_win(self):
        game_board = Board()
        game_board.make_move(1,'x')
        game_board.make_move(2,'x')
        game_board.make_move(3,'x')
        expected_winning_token = 'x'
        actual_winning_token = game_board.winner()
        self.assertEqual(expected_winning_token, actual_winning_token)

    def test_winner_with_other_combo(self):
        game_board = Board()
        game_board.make_move(7,'o')
        game_board.make_move(8, 'o')
        game_board.make_move(9, 'o')
        expected_winning_token = 'o'
        actual_winning_token = game_board.winner()
        self.assertEqual(expected_winning_token, actual_winning_token)

    def test_if_winner_returns_none_with_full_board_no_win(self):
        game_board = Board()
        game_board.make_move(1,'x')
        game_board.make_move(5,'o')
        game_board.make_move(3,'x')
        game_board.make_move(2,'o')
        game_board.make_move(8,'x')
        game_board.make_move(4,'o')
        game_board.make_move(6,'x')
        game_board.make_move(9,'o')
        game_board.make_move(7,'x')
        self.assertEqual(None,game_board.winner())

    def test_that_winner_always_returns_str_or_none(self):
        game_board = Board()
        for i in range(1,4):
            game_board.make_move(i,'x')
        self.assertEqual(str,type(game_board.winner()))
        for i in range(1,4):
            game_board.make_move(i,'o')
        self.assertEqual(str,type(game_board.winner()))
        for i in range(1,4):
            game_board.erase_move(i)
        self.assertEqual(None,game_board.winner())


class BoardIsFullTests(unittest.TestCase):

    def test_is_full_on_empty_board(self):
        self.assertEqual(False, Board().is_full())

    def test_is_full_on_non_empty_board(self):
        game_board = Board()
        game_board.make_move(1,'x')
        self.assertEqual(False, game_board.is_full())

    def test_is_full_on_full_game_board(self):
        game_board = Board()
        for i in range(1,10):
            game_board.make_move(i,'x')
        self.assertEqual(True, game_board.is_full())

class BoardAvailableMovesTests(unittest.TestCase):

    def test_if_available_moves_returns_range_ten(self):
        actual_available_moves = Board().available_moves()
        expected_available_moves = range(1,10)
        self.assertEqual(expected_available_moves, actual_available_moves)

    def test_available_moves_when_one_space_occupied(self):
        game_board = Board()
        game_board.make_move(1,'x')
        actual_available_moves = game_board.available_moves()
        expected_available_moves = range(2,10)
        self.assertEqual(expected_available_moves, actual_available_moves)

    def test_available_moves_when_all_spaces_occupied(self):
        game_board = Board()
        for space in range(1,10):
            game_board.make_move(space,'x')
        available_moves = game_board.available_moves()
        self.assertEqual([], available_moves)

class BoardEraseMoveTests(unittest.TestCase):

    def test_if_reset_erases_move(self):
        game_board = Board()
        game_board.make_move(1,'x')
        game_board.erase_move(1)
        self.assertEqual({},game_board.board_state)
