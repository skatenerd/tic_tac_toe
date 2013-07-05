from collections import OrderedDict
from ai import ImpossibleAI
from easy_ai import EasyAI
from game import Game
from no_prompt_interface import NoPromptInterface

class AiVsAiScenario(object):
    @staticmethod
    def name():
      return "AI vs AI"

    def __init__(self, user_data):
      self.user_data = user_data

    def game(self):
      return Game(self.first_ai_class()('x'), ImpossibleAI('o'))

    def first_ai_class(self):
      difficulty_response = self.user_data[AiVsAiScenario.first_ai_difficulty_prompt()]
      if difficulty_response == "easy":
        return EasyAI
      else:
        return ImpossibleAI


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
