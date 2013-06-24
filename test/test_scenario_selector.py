from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from scenario_selector import ScenarioSelector
import unittest

class ScenarioSelectorTests(unittest.TestCase):

    def test_that_scenario_mapping_works(self):
        scenario_selector = ScenarioSelector(1)
        scenario = scenario_selector.return_scenario("x","o",1,"easy")
	self.assertTrue(isinstance(scenario,HumanVsAiScenario))
        new_selector = ScenarioSelector(3)
	new_scenario = new_selector.return_scenario("x","o",1,"easy")
	self.assertTrue(isinstance(new_scenario,AiVsAiScenario))
        new_selector = ScenarioSelector(4)
	new_scenario = new_selector.return_scenario("x","o",1,"easy")
	self.assertTrue(isinstance(new_scenario,HumanoidVsAiScenario))

    def test_scenario_flags(self):
	scenario_selector = ScenarioSelector(1)
	flags = scenario_selector.scenario_flags()
	self.assertTrue(flags["difficulty_flag"])
	self.assertTrue(flags["order_flag"])
	self.assertTrue(flags["token_flag"])
