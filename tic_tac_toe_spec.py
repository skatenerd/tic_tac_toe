# Testing for Tic Tac Toe

import unittest
from tic_tac_toe import *

class BoardInitTests(unittest.TestCase):

    def test_if_new_board_is_empty_dict(self):
        self.assertEqual(dict(),Board().board_state)

class BoardMakeMoveTests(unittest.TestCase):

    def test_if_make_move_alters_board_state(self):
        empty_board_state = Board()
        sample_board = Board()
        sample_board.make_move(1,'x')
        self.assertNotEqual(empty_board_state, sample_board.board_state)

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
        actual_available_moves = Board().get_available_moves()
        expected_available_moves = range(1,10)
        self.assertEqual(expected_available_moves, actual_available_moves)

    def test_available_moves_when_one_space_occupied(self):
        game_board = Board()
        game_board.make_move(1,'x')
        actual_available_moves = game_board.get_available_moves()
        expected_available_moves = range(2,10)
        self.assertEqual(expected_available_moves, actual_available_moves)

    def test_available_moves_when_all_spaces_occupied(self):
        game_board = Board()
        for space in range(1,10):
            game_board.make_move(space,'x')
        available_moves = game_board.get_available_moves()
        self.assertEqual([], available_moves)

class BoardPiecesMatchTests(unittest.TestCase):

  def test_if_pieces_match_returns_true(self):
      game_board = Board()
      combo = [1,2,3]
      game_board.make_move(1,'x')
      game_board.make_move(2,'x')
      game_board.make_move(3,'x')
      self.assertEqual(True,game_board.pieces_match(combo))

  def test_if_pieces_match_returns_false_with_full_combo(self):
      game_board = Board()
      combo = [1,2,3]
      game_board.make_move(1,'x')
      game_board.make_move(2,'x')
      game_board.make_move(3,'o')
      self.assertEqual(False,game_board.pieces_match(combo))

  def test_if_pieces_match_returns_false_with_non_full_combo(self):
      game_board = Board()
      combo = [4,5,6]
      game_board.make_move(4,'x')
      game_board.make_move(5, 'x')
      self.assertEqual(False,game_board.pieces_match(combo))

class BoardWinnerTests(unittest.TestCase):

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

    def test_if_winner_returns_none_with_empty_board(self):
        game_board = Board()
        self.assertEqual(None, game_board.winner())

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

class PlayerInitTests(unittest.TestCase):

  def test_if_init_function_sets_token(self):
    player = Player('o')
    self.assertEqual(player.token,'o')

class AiInitTests(unittest.TestCase):

    def test_if_init_function_sets_token(self):
      computer = AI('x')
      self.assertEqual('x',computer.token)

class AiGetBestMoveTests(unittest.TestCase):

    def test_if_get_best_move_returns_five_on_second_turn(self):
      computer = AI('o')
      game_board = Board()
      human = Player('x')
      game_board.make_move(1,human.token)
      expected_move = 5
      generated_move = computer.get_best_move(game_board.board_state)
      self.assertEqual(expected_move, generated_move)

    def test_if_get_best_move_returns_one_on_first_turn(self):
      computer = AI('o')
      game_board = Board()
      expected_move = 1
      generated_move = computer.get_best_move(game_board.board_state)
      self.assertEqual(expected_move, generated_move)

if __name__ == '__main__':
    unittest.main()
