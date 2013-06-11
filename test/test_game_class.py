import unittest
import sys
sys.path.append("../")
from game import *
from board import *
import sys
from test_utils import FakePlayerInput
from player import Player

class GameRunTests(unittest.TestCase):

    def test_that_game_prints_board(self):
        fp = FakePrinter()
        display_method = fp.print_this
        game = Game(Player("x"),Player("o"),display_method)
        game.__move__(3,Player("x"))
        game.run()
        self.assertEqual(game.gameboard.__str__(),fp.last_print())

class GameMoveTests(unittest.TestCase):

    def test_that_move_alters_state(self):
        player_one = Player("x",FakePlayerInput())
        player_two = Player("o",FakePlayerInput())
        game = Game(player_one,player_two)
        p_one_move = player_one.next_move(game.gameboard)
        game.__move__(p_one_move,player_one)
        p_two_move = player_two.next_move(game.gameboard)
        game.__move__(p_two_move,player_two)
        expected_state = {p_one_move:player_one.token,
                         p_two_move:player_two.token}
        actual_state = game.gameboard.state()
        self.assertEqual(expected_state,actual_state)


class FakePrinter(object):

    def __init__(self):
        self.history = []

    def print_this(self,item):
        self.history.append(item.__str__())
        print item

    def last_print(self):
        return self.history.pop()

