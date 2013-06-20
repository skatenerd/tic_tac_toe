from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario


class ScenarioSelector(object):

    def __init__(self,player_one_token,player_two_token,order,difficulty):
        self.player_one_token = player_one_token
	self.player_two_token = player_two_token
	self.order = order
	self.difficulty = difficulty
	self.scenario_mapping = {1:HumanVsAiScenario, 3:AiVsAiScenario, 4:HumanoidVsAiScenario}

    def return_scenario(self,scenario_number):
	scenario_object = self.scenario_mapping[scenario_number]
	if scenario_number != 3:
	    return scenario_object(self.player_one_token,self.player_two_token,self.order,self.difficulty)
        return scenario_object(self.player_one_token,self.player_two_token)
