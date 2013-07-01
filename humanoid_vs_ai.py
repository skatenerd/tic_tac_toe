from game import Game
from humanoid import Humanoid
from easy_ai import EasyAI
from ai import ImpossibleAI
from human_prompt_interface import HumanPromptInterface

class HumanoidVsAiScenario(object):

    def __init__(self,player_one_token,player_two_token,
		     order=1,difficulty="impossible"):
	self.humanoid_first = {1:True,2:False}[order]
	self.token_one = player_one_token
        self.token_two = player_two_token
	self.difficulty = difficulty
	self.ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

    def setup(self):
	ai_object = self.ai_hash[self.difficulty]
	if self.humanoid_first:
            player_one = Humanoid(self.token_one)
	    player_two = ai_object(self.token_two)
	else:
            player_one = ai_object(self.token_two)
	    player_two = Humanoid(self.token_one)
	return Game(player_one,player_two)

    @staticmethod
    def flags():
	return HumanPromptInterface.prompt_flags()

    @staticmethod
    def prompts():
	return HumanPromptInterface.prompts()
