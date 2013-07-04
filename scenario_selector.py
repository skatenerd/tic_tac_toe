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

  def return_scenario(self,user_data):
    if self.scenario == HumanVsAiScenario:
      return self.scenario.game(user_data)
    if self.scenario != AiVsAiScenario and self.scenario != HumanVsHumanScenario:
      order = user_data.get("Would you like to move first or second (1,2): ")
      player_one_token, player_two_token = self.__assign_tokens__(user_data)
      difficulty = user_data.get("Would you like to play against an easy or impossible ai: ")
      return self.scenario(player_one_token,player_two_token,order,difficulty)
    elif self.scenario == AiVsAiScenario and user_data.get("What difficulty would you like the first ai to be (easy,impossible): ") == "easy":
      return EasyVsImpossibleAiScenario()
    return self.scenario()

  def __assign_tokens__(self,user_data):
    if user_data.get("Would you like to move first or second (1,2): ") == 1:
      player_one_token = user_data.get("Would you like to play as x or o: ")
      player_two_token = self.__other_token__(player_one_token)
    else:
      player_two_token = user_data.get("Would you like to play as x or o: ")
      player_one_token = self.__other_token__(player_two_token)
    return [player_one_token,player_two_token]

  def __other_token__(self,token):
    return {"x":"o","o":"x"}[token]

  def scenario_flags(self):
    return self.scenario.flags()

  def scenario_prompts(self):
    return self.scenario.prompts()
