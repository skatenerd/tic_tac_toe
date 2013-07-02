import unittest
from easy_vs_impossible_ai import EasyVsImpossibleAiScenario

class EasyVsImpossibleAiScenarioTests(unittest.TestCase):

    def test_scenario_returns_game(self):
	scenario = EasyVsImpossibleAiScenario()
	game = scenario.setup()
	self.assertEqual("x",game.player_one.token)

