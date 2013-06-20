import unittest
from scenario import Scenario
from humanoid_vs_ai import HumanoidVsAiScenario
from game import Game
from humanoid import Humanoid
from easy_ai import EasyAI

class HumanoidVsAiScenarioInitTests(unittest.TestCase):

    def test_that_it_sets_tokens_properly(self):
        scenario = HumanoidVsAiScenario("x","o",1,"impossible")
	self.assertEqual("x",scenario.player_one_token)
	self.assertEqual("o",scenario.player_two_token)

    def test_that_it_sets_order_and_difficulty(self):
	scenario = HumanoidVsAiScenario("x","o",1,"impossible")
	var_and_method_list = dir(scenario)
	self.assertTrue("human_first" in var_and_method_list)
	self.assertTrue("difficulty" in var_and_method_list)
	
class HumanoidVsAiScenarioSetupTests(unittest.TestCase):
    
    def test_that_it_returns_game_object(self):
	scenario = HumanoidVsAiScenario("x","o",1,"impossible")
	game = scenario.setup()
	self.assertTrue(isinstance(game,Game))
	
    def test_that_it_set_correct_player_order(self):
	scenario = HumanoidVsAiScenario("x","o",2,"impossible")
	game = scenario.setup()
	player_two = game.player_two
	self.assertTrue(isinstance(player_two,Humanoid))
	
    def test_that_it_works_with_easy_ai(self):
	scenario = HumanoidVsAiScenario("x","o",1,"easy")
	game = scenario.setup()
	player_two = game.player_two
	self.assertTrue(isinstance(player_two,EasyAI))
