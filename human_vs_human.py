from player import Player
from game import Game

class HumanVsHumanScenario(object):

    token_flag = False
    difficulty_flag = False
    order_flag = False

    def setup(self):
        player_one = Player("x")
	player_two = Player("o")
	return Game(player_one,player_two)

    @staticmethod
    def flags():
        flag_dict = {"difficulty_flag":HumanVsHumanScenario.difficulty_flag,
		     "token_flag":HumanVsHumanScenario.token_flag,
		     "order_flag":HumanVsHumanScenario.order_flag}
	return flag_dict
