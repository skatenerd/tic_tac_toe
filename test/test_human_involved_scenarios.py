import unittest
from game import Game
from ai import ImpossibleAI
from easy_ai import EasyAI
from player import HumanPlayer
from human_vs_ai import HumanVsAiScenario

class SetupTests(unittest.TestCase):

    def test_setup_returns_game(self):
	scenario = HumanVsAiScenario("x","o")
	game = scenario.setup()
	self.assertTrue(isinstance(game,Game))

    def test_setup_assigns_game_with_correct_order(self):
	scenario = HumanVsAiScenario("x","o")
	game = scenario.setup()
	self.assertTrue(not isinstance(game.player_one,ImpossibleAI))
	self.assertTrue(isinstance(game.player_two,ImpossibleAI))

        scenario = HumanVsAiScenario("o","x")
	game = scenario.setup()
	self.assertTrue(not isinstance(game.player_one,ImpossibleAI))
	self.assertTrue(isinstance(game.player_two,ImpossibleAI))
  
    def test_that_scenario_works_with_easy_ai(self):
        scenario = HumanVsAiScenario("x","o",difficulty="easy")
	scenario.human_first = True
	game = scenario.setup()
	self.assertTrue(isinstance(game.player_two,EasyAI))
