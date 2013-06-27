from game import Game
from humanoid import Humanoid
from human_vs_ai import HumanVsAiScenario
from easy_ai import EasyAI
from ai import ImpossibleAI
from human_prompt_interface import HumanPromptInterface

class HumanoidVsAiScenario(object):

    def __init__(self,player_one_token,player_two_token,
		     order=1,difficulty="impossible"):
	self.humanoid_first = {1:True,2:False}[order]
        self.human_behavior_implementation = HumanPromptInterface(player_one_token,player_two_token,
			                                          self.humanoid_first,difficulty) 

    def setup(self):
	return self.human_behavior_implementation.setup(Humanoid)

    @staticmethod
    def flags():
	return HumanPromptInterface.prompt_flags()
