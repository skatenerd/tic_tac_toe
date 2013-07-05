from collections import OrderedDict
from ai import ImpossibleAI
from game import Game
from no_prompt_interface import NoPromptInterface

class AiVsAiScenario(object):
    @staticmethod
    def name():
      return "AI vs AI"

    def __init__(self, user_data):
      self.user_data = user_data

    def game(self):
      return Game(ImpossibleAI('x'), ImpossibleAI('o'))

    @staticmethod
    def first_ai_difficulty_prompt():
      return "What difficulty would you like the first ai to be (easy,impossible): "

    @staticmethod
    def prompts():
      difficulty_prompt = {
          AiVsAiScenario.first_ai_difficulty_prompt():
          ("easy","impossible")
      }
      return OrderedDict(difficulty_prompt)
