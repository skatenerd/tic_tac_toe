import unittest
from human_prompt_interface import HumanPromptInterface
from game import Game
from ai import ImpossibleAI
from easy_ai import EasyAI
from player import HumanPlayer

class HumanPromptInterfaceFlagsTests(unittest.TestCase):

    def test_that_it_returns_appropriate_flags(self):
	interface = HumanPromptInterface("x","o")
	flags = interface.prompt_flags()
	self.assertTrue("token_flag" in flags)
	self.assertTrue("difficulty_flag" in flags)
	self.assertTrue("order_flag" in flags)

class HumanVsAiSetupTests(unittest.TestCase):

    def test_setup_returns_game(self):
	interface = HumanPromptInterface("x","o")
	game = interface.setup()
	self.assertTrue(isinstance(game,Game))

    def test_setup_assigns_game_with_correct_order(self):
	interface = HumanPromptInterface("x","o")
	game = interface.setup()
	self.assertTrue(not isinstance(game.player_one,ImpossibleAI))
	self.assertTrue(isinstance(game.player_two,ImpossibleAI))

        interface = HumanPromptInterface("o","x")
	game = interface.setup()
	self.assertTrue(not isinstance(game.player_one,ImpossibleAI))
	self.assertTrue(isinstance(game.player_two,ImpossibleAI))
  
    def test_that_scenario_works_with_easy_ai(self):
        interface = HumanPromptInterface("x","o",difficulty="easy")
	interface.human_first = True
	game = interface.setup(HumanPlayer)
	self.assertTrue(isinstance(game.player_two,EasyAI))
