from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from human_vs_human import HumanVsHumanScenario
from easy_vs_impossible_ai import EasyVsImpossibleAiScenario

class ScenarioSelector(object):

  scenario_list = {
      1: HumanVsAiScenario,
      2: HumanVsHumanScenario,
      3: AiVsAiScenario,
      4: HumanoidVsAiScenario
  }

  def __init__(self,scenario_number):
    self.scenario = ScenarioSelector.scenario_list[scenario_number]

  def return_game(self,user_data):
    return self.scenario(user_data).game()

  def scenario_prompts(self):
    return self.scenario.prompts()
