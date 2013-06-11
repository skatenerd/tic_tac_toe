import unittest
import sys
sys.path.append("../")
from game import *
from board import *
import sys
from playerinput import FakePlayerInput
from player import Player

class GameRunTests(unittest.TestCase):

    def test_that_init_works(self):
        game = Game(Player("x"),Player("o"))
        self.assertEqual(dict(),game.gameboard.state())
        self.assertIsInstance(game.player_one,Player)
        self.assertIsInstance(game.player_two,Player)

    def test_that_loop_works(self):
        player_o = Player("o",FakePlayerInput())
        player_x = Player("x",FakePlayerInput())
        game = Game(player_o,player_x)
        game.run()
        self.assertEqual(True,game.over())

class GameMoveTests(unittest.TestCase):

    def test_that_move_alters_state(self):
        player_one = Player("x",FakePlayerInput())
        player_two = Player("o",FakePlayerInput())
        game = Game(player_one,player_two)
        p_one_move = player_one.next_move(game.gameboard)
        game.move(p_one_move,player_one)
        p_two_move = player_two.next_move(game.gameboard)
        game.move(p_two_move,player_two)
        expected_state = {p_one_move:player_one.token,
                         p_two_move:player_two.token}
        actual_state = game.gameboard.state()
        self.assertEqual(expected_state,actual_state)

