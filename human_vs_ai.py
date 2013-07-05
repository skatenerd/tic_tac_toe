from player import HumanPlayer
from human_prompt_interface import HumanPromptInterface
from easy_ai import EasyAI
from ai import ImpossibleAI
from game import Game

class Token(object):
  def __init__(self, name):
    self.name = name

  def other(self):
    other_name = {"x":"o","o":"x"}[self.name]
    return Token(other_name)

class HumanVsAiScenario(object):

  @staticmethod
  def name():
    return "Human vs AI"

  def __init__(self, user_data):
    self.ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}
    self.user_data = user_data

  def game(self):
    order = self.user_data[HumanPromptInterface.order_prompt()]
    token = self.user_data[HumanPromptInterface.token_prompt()]
    difficulty = self.user_data[HumanPromptInterface.difficulty_prompt()]
    if order == 1:
      return Game(self.human_player(token), self.ai_player(difficulty, token))
    else:
      return Game(self.ai_player(difficulty, token), self.human_player(token))

  def ai_player(self, difficulty, token):
    klass =  self.ai_hash[difficulty]
    ai_token = Token(token).other().name
    return klass(ai_token)

  def human_player(self, token):
    return HumanPlayer(token)

  @staticmethod
  def prompts():
    return HumanPromptInterface.prompts()
