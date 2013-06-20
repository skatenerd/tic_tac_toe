from scenario import Scenario
from game import Game
from easy_ai import EasyAI
from ai import AI
from player import Player

class HumanVsAiScenario(Scenario):

	def __init__(self,player_one_token,player_two_token,
		     order=1,difficulty="impossible"):
	    super(HumanVsAiScenario,self).__init__(player_one_token,player_two_token) 
	    self.ai_hash = {"easy":EasyAI,"impossible":AI}
	    self.human_first = {1:True,2:False}[order] 
	    self.difficulty = difficulty

	def setup(self):
	    ai_object = self.ai_hash[self.difficulty]
	    if self.human_first:
	        player_one = Player(self.player_one_token)
		player_two = ai_object(self.player_two_token)
	    else:
		player_one = ai_object(self.player_one_token)
		player_two = Player(self.player_two_token)
            return Game(player_one,player_two)
