class HumanPromptInterface(object):

    @staticmethod
    def prompt_flags(**more_flags):
	prompt_flags =  {"difficulty_flag":True,
	                 "token_flag":True,
		         "order_flag":True}
	prompt_flags.update(more_flags)
        return prompt_flags

