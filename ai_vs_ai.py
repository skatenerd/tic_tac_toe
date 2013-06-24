from ai import AI
from game import Game
from scenario import Scenario

class AiVsAiScenario(object):

    token_flag = False
    difficulty_flag = False
    order_flag = False

    def setup(self):
        player_one = AI("x")
	player_two = AI("o")
	return Game(player_one,player_two)

    @staticmethod
    def flags():
        flag_dict = {"difficulty_flag":AiVsAiScenario.difficulty_flag, 
		     "token_flag":AiVsAiScenario.token_flag,
		     "order_flag":AiVsAiScenario.order_flag}
	return flag_dict
