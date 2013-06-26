import unittest
from easy_ai import EasyAI
from ai import ImpossibleAI
from game import Game
from board import Board

class AiDifficultyTests(unittest.TestCase):

    def test_that_it_doesnt_block(self):
	board = Board()
	computer = EasyAI("x")
	board.board_state = {1:"o",2:"o",4:"x"}
	self.assertTrue(computer.next_move(board) != 3)

    def test_that_it_wont_beat_impossible_ai(self):
	board = Board()
	computer = EasyAI("x")
	computer_two = ImpossibleAI("o")
	game = Game(computer,computer_two)
	game.run()
	self.assertTrue(game.gameboard.winner() != "x")

    def test_easy_ai_has_token(self):
        computer = EasyAI("o")
        self.assertEqual("o",computer.token)
