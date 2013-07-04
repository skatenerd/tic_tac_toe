from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from scenario_selector import ScenarioSelector
import unittest

class ScenarioSelectorTests(unittest.TestCase):

    def setUp(self):
      self.user_data = {"Would you like to play as x or o: ": "x",
                        "Would you like to move first or second (1,2): ": 1,
                        "Would you like to play against an easy or impossible ai: ": "easy"}

    def test_second_player_works(self):
      scenario_selector = ScenarioSelector(1)
      self.user_data["Would you like to move first or second (1,2): "] = 2
      game = scenario_selector.return_scenario(self.user_data)
      self.assertEqual("x", game.player_two.token)

    def test_first_player_works(self):
      scenario_selector = ScenarioSelector(1)
      game = scenario_selector.return_scenario(self.user_data)
      self.assertEqual("x", game.player_one.token)

    def test_scenario_flags(self):
      scenario_selector = ScenarioSelector(1)
      flags = scenario_selector.scenario_flags()
      self.assertTrue(flags["difficulty_flag"])
      self.assertTrue(flags["order_flag"])
      self.assertTrue(flags["token_flag"])

    def assertFlagsFalse(self,flag_dictionary):
      for flag in flag_dictionary.values():
        self.assertFalse(flag)

