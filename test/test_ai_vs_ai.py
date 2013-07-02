import unittest
from no_prompt_interface import NoPromptInterface
from game import Game
from player import HumanPlayer

class NoPromptInterfaceTests(unittest.TestCase):

    def test_flags_are_false(self):
	interface = NoPromptInterface
	flag_dict = interface.flags()
	for flag in flag_dict:
	    self.assertFalse(flag_dict[flag])

    def test_setup_should_return_game(self):
	player = HumanPlayer
	interface = NoPromptInterface()
	game = interface.setup(player)
        self.assertEqual("x",game.player_one.token)	
    
