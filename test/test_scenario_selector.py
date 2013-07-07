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

  def scenario_prompts(self):
    return ("Please choose a scenario:\n" +
              "(1) Human vs AI\n" +
              "(2) Human vs Human\n" +
              "(3) AI vs AI\n" +
              "(4) Humanoid vs AI")

  def test_prompts_present(self):
    fake_printer = FakePrinter()
    mock_input = MockUserInput([1])
    selector = ScenarioSelector(mock_input, fake_printer)
    scenario_class = selector.scenario_class()
    self.assertEqual(scenario_class, HumanVsAiScenario)

    history = fake_printer.history
    self.assertEqual(history[0], self.scenario_prompts())

