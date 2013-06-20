import unittest
from human_vs_ai import HumanVsAiScenario
from scenario import Scenario
from game import Game
from ai import AI
from easy_ai import EasyAI

class HumanVsAiInitTests(unittest.TestCase):

    def test_that_it_inherits_from_scenario(self):
	new_scenario = HumanVsAiScenario("x","o")
	self.assertTrue(isinstance(new_scenario,Scenario))
	self.assertEqual("x",new_scenario.player_one_token)
	self.assertEqual("o",new_scenario.player_two_token)
      
    def test_that_it_has_human_first_var(self):
	new_scenario = HumanVsAiScenario("x","o")
	var_and_method_list = dir(new_scenario)
	self.assertTrue("human_first" in var_and_method_list)

    def test_that_it_has_ai_hash_var(self):
	new_scenario = HumanVsAiScenario("x","o")
	var_and_method_list = dir(new_scenario)
	self.assertTrue("ai_hash" in var_and_method_list)

    def test_that_it_has_difficulty_var(self):
	new_scenario = HumanVsAiScenario("x","o")
	var_and_method_list = dir(new_scenario)
	self.assertTrue("difficulty" in var_and_method_list)

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
        
	new_scenario = HumanVsAiScenario("o","x")
	new_scenario.human_first = False
	game = new_scenario.setup()
        self.assertTrue(isinstance(game.player_one,AI))
	self.assertTrue(not isinstance(game.player_two,AI))
  
    def test_that_scenario_works_with_easy_ai(self):
        new_scenario = HumanVsAiScenario("x","o")
        new_scenario.difficulty = "easy"
	new_scenario.human_first = True
	game = new_scenario.setup()
	self.assertTrue(isinstance(game.player_two,EasyAI))
