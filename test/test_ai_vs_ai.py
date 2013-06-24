import unittest
from ai_vs_ai import AiVsAiScenario
from game import Game
from ai import AI

class AiVsAiScenarioInitTests(unittest.TestCase):

    def test_flags_are_false(self):
	scenario = AiVsAiScenario()
	flag_dict = scenario.flags()
	for flag in flag_dict:
	    self.assertFalse(flag_dict[flag])
