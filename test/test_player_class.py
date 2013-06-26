import sys
sys.path.append("../")
from player import *
import unittest

class PlayerInitTests(unittest.TestCase):

    def test_if_init_function_sets_token(self):
        player = HumanPlayer('o')
        self.assertEqual(player.token,'o')

    def test_if_init_function_set_opponent_token(self):
        player = HumanPlayer('o')
        self.assertEqual('x',player.opponent_token)
        player_two = HumanPlayer('x')
        self.assertEqual('o',player_two.opponent_token)

