from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from human_vs_human import HumanVsHumanScenario

class ScenarioSelector(object):

    def __init__(self,scenario):
	self.scenario_mapping = {HumanVsAiScenario:1,HumanVsHumanScenario:2, AiVsAiScenario:3, HumanoidVsAiScenario:4}
	self.scenario = scenario
	self.scenario_number = self.scenario_mapping[scenario]
        
    def return_scenario(self,user_data):
	if self.scenario_number != 3 and self.scenario_number != 2:
	    order = user_data.get("Would you like to move first or second (1,2): ")
	    if order == 1:
	        player_one_token = user_data.get("Would you like to play as x or o: ")
	        player_two_token = {"x":"o","o":"x"}[player_one_token]
	    else:
		player_two_token = user_data.get("Would you like to play as x or o: ")
		player_one_token = {"x":"o","o":"x"}[player_two_token]
	    difficulty = user_data.get("Would you like to play against an easy or impossible ai: ")
	    print order
	    return self.scenario(player_one_token,player_two_token,order,difficulty)
        return self.scenario()
    
    def scenario_flags(self):
        return self.scenario.flags()	

    def scenario_prompts(self):
	return self.scenario.prompts()
