from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from human_vs_human import HumanVsHumanScenario

class ScenarioSelector(object):

    def __init__(self,scenario_number):
	self.scenario_mapping = {1:HumanVsAiScenario,2:HumanVsHumanScenario, 3:AiVsAiScenario, 4:HumanoidVsAiScenario}
	self.scenario = self.scenario_mapping[scenario_number]
	self.scenario_number = scenario_number

    def return_scenario(self,player_one_token,player_two_token,order,difficulty):
	if self.scenario_number != 3 and self.scenario_number != 2:
	    return self.scenario(player_one_token,player_two_token,order,difficulty)
        return self.scenario()
    
    def scenario_flags(self):
        return self.scenario.flags()	
