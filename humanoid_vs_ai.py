from game import Game
from human_vs_ai import Token
from humanoid import Humanoid
from easy_ai import EasyAI
from ai import ImpossibleAI
from human_prompt_interface import HumanPromptInterface

class HumanoidVsAiScenario(object):

    ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

    @staticmethod
    def name():
      return "Humanoid vs AI"


    @staticmethod
    def game(user_data):
      order = user_data[HumanPromptInterface.order_prompt()]
      token = user_data[HumanPromptInterface.token_prompt()]
      difficulty = user_data[HumanPromptInterface.difficulty_prompt()]
      if order == 1:
        return Game(HumanoidVsAiScenario.human_player(token), HumanoidVsAiScenario.ai_player(difficulty, token))
      else:
        return Game(HumanoidVsAiScenario.ai_player(difficulty, token), HumanoidVsAiScenario.human_player(token))

    @staticmethod
    def ai_player(difficulty, token):
      klass =  HumanoidVsAiScenario.ai_hash[difficulty]
      ai_token = Token(token).other().name
      return klass(ai_token)

    @staticmethod
    def human_player(token):
      return Humanoid(token)


    def __init__(self,player_one_token,player_two_token,
                    order=1,difficulty="impossible"):
       self.humanoid_first = {1:True,2:False}[order]
       self.token_one = player_one_token
       self.token_two = player_two_token
       self.difficulty = difficulty
       self.ai_hash = {"easy":EasyAI,"impossible":ImpossibleAI}

    def setup(self):
      ai_object = self.ai_hash[self.difficulty]
      if self.humanoid_first:
        player_one = Humanoid(self.token_one)
        player_two = ai_object(self.token_two)
      else:
        player_one = ai_object(self.token_two)
        player_two = Humanoid(self.token_one)
      return Game(player_one,player_two)

    @staticmethod
    def flags():
      return HumanPromptInterface.prompt_flags()

    @staticmethod
    def prompts():
      return HumanPromptInterface.prompts()
