from ai import ImpossibleAI
from game import Game
from no_prompt_interface import NoPromptInterface

class AiVsAiScenario(object):

    def setup(self):
        return NoPromptInterface().setup(ImpossibleAI)

    @staticmethod
    def flags():
        return NoPromptInterface.flags()

    @staticmethod
    def prompts():
	return NoPromptInterface.prompts()
