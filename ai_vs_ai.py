from ai import ImpossibleAI
from game import Game
from no_prompt_interface import NoPromptInterface

class AiVsAiScenario(object):
    @staticmethod
    def name():
      return "AI vs AI"

    def setup(self):
        return NoPromptInterface().setup(ImpossibleAI)

    @staticmethod
    def flags():
        return NoPromptInterface.flags()

    @staticmethod
    def prompts():
	difficulty_prompt = {"What difficulty would you like the first ai to be (easy,impossible): ":
			     ("easy","impossible")}
	return NoPromptInterface.prompts(difficulty_prompt)
