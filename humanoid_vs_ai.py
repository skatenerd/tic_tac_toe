from scenario import Scenario
from game import Game
from humanoid import Humanoid
from ai import AI
from easy_ai import EasyAI
from human_vs_ai import HumanVsAiScenario

class HumanoidVsAiScenario(HumanVsAiScenario):

    def setup(self):
	ai_object = self.ai_hash[self.difficulty]
	if self.human_first:
	    player_one = Humanoid(self.player_one_token)
	    player_two = ai_object(self.player_two_token)
	else:
	    player_one = ai_object(self.player_one_token)
	    player_two = Humanoid(self.player_two_token)
	return Game(player_one,player_two)
