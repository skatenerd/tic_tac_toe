import unittest
from human_vs_ai import HumanVsAiScenario
from game import Game
from ai import AI
from easy_ai import EasyAI

class HumanVsAiScenarioFlagsTests(unittest.TestCase):

    def test_that_it_returns_appropriate_flags(self):
	new_scenario = HumanVsAiScenario("x","o")
	flags = new_scenario.flags()
	self.assertTrue("token_flag" in flags)
	self.assertTrue("difficulty_flag" in flags)
	self.assertTrue("order_flag" in flags)

class HumanVsAiSetupTests(unittest.TestCase):

    def test_setup_returns_game(self):
	new_scenario = HumanVsAiScenario("x","o")
	game = new_scenario.setup()
	self.assertTrue(isinstance(game,Game))

    def test_setup_assigns_game_with_correct_order(self):
	new_scenario = HumanVsAiScenario("x","o")
	game = new_scenario.setup()
	self.assertTrue(not isinstance(game.player_one,AI))
	self.assertTrue(isinstance(game.player_two,AI))

        new_scenario = HumanVsAiScenario("o","x")
	game = new_scenario.setup()
	self.assertTrue(not isinstance(game.player_one,AI))
	self.assertTrue(isinstance(game.player_two,AI))
  
    def test_that_scenario_works_with_easy_ai(self):
        new_scenario = HumanVsAiScenario("x","o",difficulty="easy")
	new_scenario.human_first = True
	game = new_scenario.setup()
	self.assertTrue(isinstance(game.player_two,EasyAI))
