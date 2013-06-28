from easy_ai import EasyAI
from ai import ImpossibleAI
from game import Game
from player import HumanPlayer
from humanoid import Humanoid

class GameFactory(object):

    def __init__(self,token_one,token_two,
		 human_first=True,difficulty="impossible"):
        self.token_one = token_one
	self.token_two = token_two
	self.human_first = human_first
	self.difficulty = difficulty
	self.ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

    def setup(self,
