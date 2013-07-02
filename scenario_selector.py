from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from human_vs_human import HumanVsHumanScenario
from easy_vs_impossible_ai import EasyVsImpossibleAiScenario

class ScenarioSelector(object):

    def __init__(self,scenario):
	self.scenario_mapping = {HumanVsAiScenario:1,HumanVsHumanScenario:2, AiVsAiScenario:3, HumanoidVsAiScenario:4}
	self.scenario = scenario
	self.scenario_number = self.scenario_mapping[scenario]
        
    def return_scenario(self,user_data):
	if self.scenario_number != 3 and self.scenario_number != 2:
	    order = user_data.get("Would you like to move first or second (1,2): ")
            player_one_token, player_two_token = self.__assign_tokens__(user_data)
	    difficulty = user_data.get("Would you like to play against an easy or impossible ai: ")
	    return self.scenario(player_one_token,player_two_token,order,difficulty)
        elif self.scenario_number == 3 and user_data.get("What difficulty would you like the first ai to be (easy,impossible): ") == "easy":
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
