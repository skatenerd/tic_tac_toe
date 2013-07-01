from game import Game
from collections import OrderedDict

class NoPromptInterface(object):

    def setup(self,player_object):
	return Game(player_object("x"),player_object("o"))

    @staticmethod
    def flags(**more_flags):
        prompt_flags = {"token_flag":False,
	                "difficulty_flag":False,
		        "order_flag":False}
	prompt_flags.update(more_flags)
	return prompt_flags

    @staticmethod
    def prompts(**more_prompts):
	prompt_hash = OrderedDict()
	for prompt in more_prompts:
            prompt_hash.update(prompt)
	return prompt_hash
