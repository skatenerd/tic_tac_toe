from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from scenario_selector import ScenarioSelector
import unittest

class ScenarioSelectorTests(unittest.TestCase):

    def test_that_scenario_mapping_works(self):
        scenario_selector = ScenarioSelector("x","o",1,"impossible")
        scenario = scenario_selector.return_scenario(1)
	self.assertTrue(isinstance(scenario,HumanVsAiScenario))
        new_selector = ScenarioSelector("x","o",1,"easy")
	new_scenario = new_selector.return_scenario(3)
	self.assertTrue(isinstance(new_scenario,AiVsAiScenario))
        new_selector = ScenarioSelector("x","o",2,"impossible")
	new_scenario = new_selector.return_scenario(4)
	self.assertTrue(isinstance(new_scenario,HumanoidVsAiScenario))
