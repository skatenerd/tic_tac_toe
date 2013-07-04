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
  ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

  @staticmethod
  def name():
    return "Human vs AI"

  @staticmethod
  def game(user_data):
    order = user_data[HumanPromptInterface.order_prompt()]
    token = user_data[HumanPromptInterface.token_prompt()]
    difficulty = user_data[HumanPromptInterface.difficulty_prompt()]
    if order == 1:
      return Game(HumanVsAiScenario.human_player(token), HumanVsAiScenario.ai_player(difficulty, token))
    else:
      return Game(HumanVsAiScenario.ai_player(difficulty, token), HumanVsAiScenario.human_player(token))

  @staticmethod
  def ai_player(difficulty, token):
    klass =  HumanVsAiScenario.ai_hash[difficulty]
    ai_token = Token(token).other().name
    return klass(ai_token)

  @staticmethod
  def human_player(token):
    return HumanPlayer(token)

  def __init__(self,player_one_token,player_two_token,
    order=1,difficulty="impossible"):
    self.human_first = {1:True,2:False}[order]
    self.token_one = player_one_token
    self.token_two = player_two_token
    self.difficulty = difficulty
    self.ai_hash = HumanVsAiScenario.ai_hash

  def setup(self):
    ai_object = self.ai_hash[self.difficulty]
    if self.human_first:
        player_one = HumanPlayer(self.token_one)
        player_two = ai_object(self.token_two)
    else:
        player_one = ai_object(self.token_one)
        player_two = HumanPlayer(self.token_two)
    return Game(player_one,player_two)

  @staticmethod
  def flags():
    return HumanPromptInterface.prompt_flags()

  @staticmethod
  def prompts():
    return HumanPromptInterface.prompts()
