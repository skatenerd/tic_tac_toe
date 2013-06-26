from player import HumanPlayer
from game import Game
from no_human_involvement import NoHumanInvolvementInterface

class HumanVsHumanScenario(object):

    token_flag = False
    difficulty_flag = False
    order_flag = False

    def __init__(self):
	self.interface = NoHumanInvolvementInterface()

    def setup(self):
	player_one = HumanPlayer("x")
	player_two = HumanPlayer("o")
	return Game(player_one,player_two)

    @staticmethod
    def flags():
        return {"difficulty_flag":False,
		"token_flag":False,
		"order_flag":False}
