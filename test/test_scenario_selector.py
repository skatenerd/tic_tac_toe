from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from scenario_selector import ScenarioSelector
from test_utils import *
import unittest

class ScenarioSelectorTests(unittest.TestCase):

  def test_returns_human_vs_ai_scenario(self):
    mock_input = MockUserInput([1])
    selector = ScenarioSelector(mock_input)
    scenario_class = selector.scenario_class()
    self.assertEqual(scenario_class, HumanVsAiScenario)

  def test_requires_valid_input(self):
    mock_input = MockUserInput([5, 4])
    selector = ScenarioSelector(mock_input)
    scenario_class = selector.scenario_class()
    self.assertEqual(scenario_class, HumanoidVsAiScenario)

