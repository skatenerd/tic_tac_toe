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
	return self.interface.setup(HumanPlayer)

    @staticmethod
    def flags():
        flag_dict = {"difficulty_flag":HumanVsHumanScenario.difficulty_flag,
		     "token_flag":HumanVsHumanScenario.token_flag,
		     "order_flag":HumanVsHumanScenario.order_flag}
	return flag_dict
