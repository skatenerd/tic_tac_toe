from player import HumanPlayer
from human_prompt_interface import HumanPromptInterface

class HumanVsAiScenario(object):

    def __init__(self,player_one_token,player_two_token,
		     order=1,difficulty="impossible"):
         self.human_first = {1:True,2:False}[order] 
	 self.interface = HumanPromptInterface(player_one_token,player_two_token,
			                                           self.human_first,difficulty)

    def setup(self):
        interface = self.interface
	return interface.setup(HumanPlayer)

    @staticmethod
    def flags():
        return HumanPromptInterface.prompt_flags()
