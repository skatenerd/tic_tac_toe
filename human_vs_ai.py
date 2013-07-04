from player import HumanPlayer
from human_prompt_interface import HumanPromptInterface
from easy_ai import EasyAI
from ai import ImpossibleAI
from game import Game

class HumanVsAiScenario(object):
    @staticmethod
    def name():
      return "Human vs AI"

    def __init__(self,player_one_token,player_two_token,
		     order=1,difficulty="impossible"):
         self.human_first = {1:True,2:False}[order]
	 self.token_one = player_one_token
	 self.token_two = player_two_token
	 self.difficulty = difficulty
	 self.ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

    def setup(self):
	ai_object = self.ai_hash[self.difficulty]
	if self.human_first:
	    player_one = HumanPlayer(self.token_one)
	    player_two = ai_object(self.token_two)
	else:
	    player_one = ai_object(self.token_one)
	    player_two = HumanPlayer(self.token_two)
	return Game(player_one,player_two)

    @staticmethod
    def flags():
        return HumanPromptInterface.prompt_flags()

    @staticmethod
    def prompts():
	return HumanPromptInterface.prompts()
