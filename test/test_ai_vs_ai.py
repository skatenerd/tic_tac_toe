import unittest
from ai_vs_ai import AiVsAiScenario
from game import Game
from ai import AI

class AiVsAiScenarioInitTests(unittest.TestCase):

    def test_that_scenario_has_tokens(self):
        scenario = AiVsAiScenario("x","o")
        self.assertTrue("x",scenario.player_one_token)
	self.assertTrue("o",scenario.player_two_token)

    def test_that_setup_returns_game_with_ai_players(self):
        scenario = AiVsAiScenario("x","o")
	game = scenario.setup()
	player_one = game.player_one
	player_two = game.player_two
	self.assertTrue(isinstance(player_one,AI))
	self.assertTrue(isinstance(player_two,AI))

