import sys
sys.path.append("../")
from playerinput import FakePlayerInput
from board import Board
import unittest

class PlayerInputTests(unittest.TestCase):

  def test_fake_player_input_returns_move_in_available_moves(self):
      board = Board()
      board.make_move(1,'x')
      fake_input = FakePlayerInput()
      move = fake_input.output(board)
      self.assertEqual(True,move in board.available_moves())


  def test_fake_player_knows_board_state(self):
      board = Board()
      fake_input = FakePlayerInput()
      for i in range(1,10):
          board.make_move(i,"x")
      self.assertRaises(IndexError,fake_input.output, board)