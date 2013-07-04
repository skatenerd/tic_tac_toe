from collections import OrderedDict

class HumanPromptInterface(object):

    @staticmethod
    def prompt_flags(**more_flags):
	prompt_flags =  {"difficulty_flag":True,
	                 "token_flag":True,
		         "order_flag":True}
	prompt_flags.update(more_flags)
        return prompt_flags

    @staticmethod
    def order_prompt():
      return "Would you like to move first or second (1,2): "

    @staticmethod
    def token_prompt():
      return "Would you like to play as x or o: "

    @staticmethod
    def difficulty_prompt():
      return "Would you like to play against an easy or impossible ai: "

    @staticmethod
    def prompts(*more_prompts):
      current_prompts = OrderedDict()
      current_prompts[HumanPromptInterface.order_prompt()] = (1,2)
      current_prompts[HumanPromptInterface.token_prompt()] = ("x","o")
      current_prompts[HumanPromptInterface.difficulty_prompt()] = ("easy","impossible")
      for prompt_hash in more_prompts:
          current_prompts.update(prompt_hash)
      return current_prompts

