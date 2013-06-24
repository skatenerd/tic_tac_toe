from game import Game
from easy_ai import EasyAI
from ai import AI
from player import Player

class HumanVsAiScenario(object):
   
    token_flag = True
    difficulty_flag = True
    order_flag = True

    def __init__(self,player_one_token,player_two_token,
		     order=1,difficulty="impossible"):
         self.player_one_token = player_one_token
	 self.player_two_token = player_two_token
	 self.difficulty = difficulty
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

    @staticmethod
    def flags():
        flag_dict = {"difficulty_flag":HumanVsAiScenario.difficulty_flag,
		     "token_flag":HumanVsAiScenario.token_flag,
	             "order_flag":HumanVsAiScenario.order_flag}
	return flag_dict

