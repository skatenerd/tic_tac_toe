from easy_ai import EasyAI
from ai import ImpossibleAI
from game import Game
from player import HumanPlayer

class HumanBehaviorInterface(object):

    def __init__(self,token_one,token_two,
		 human_first=True,difficulty="impossible"):
	self.token_one = token_one
	self.token_two = token_two
	self.human_first = human_first
	self.difficulty = difficulty
	self.ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

    def setup(self,class_name=HumanPlayer):
	ai_object = self.ai_hash[self.difficulty]
	if self.human_first:
	    player_one = class_name(self.token_one)
	    player_two = ai_object(self.token_two)
	else:
	    player_one = ai_object(self.token_one)
	    player_two = class_name(self.token_two)
	return Game(player_one,player_two)

    @staticmethod
    def prompt_flags():
	return {"difficulty_flag":True,
	        "token_flag":True,
		"order_flag":True}

