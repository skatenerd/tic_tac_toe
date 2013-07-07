from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from human_vs_human import HumanVsHumanScenario
from easy_vs_impossible_ai import EasyVsImpossibleAiScenario
from playerinput import InputValidator

class ScenarioSelector(object):

  scenario_list = {
      1: HumanVsAiScenario,
      2: HumanVsHumanScenario,
      3: AiVsAiScenario,
      4: HumanoidVsAiScenario
  }

  def __init__(self, user_input):
    self.user_input = user_input

  def scenario_class(self):
    the_input = InputValidator.return_valid_response(self.user_input, ScenarioSelector.scenario_list.keys())
    return ScenarioSelector.scenario_list[the_input]

