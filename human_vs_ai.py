from player import HumanPlayer
from human_behavior import HumanBehaviorInterface

class HumanVsAiScenario(object):

    def __init__(self,player_one_token,player_two_token,
		     order=1,difficulty="impossible"):
         self.human_first = {1:True,2:False}[order] 
	 self.human_behavior_implementation = HumanBehaviorInterface(player_one_token,player_two_token,
			                                           self.human_first,difficulty)

    def setup(self):
	return self.human_behavior_implementation.setup(HumanPlayer)

    @staticmethod
    def flags():
        return HumanBehaviorInterface.prompt_flags()
