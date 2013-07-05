from game import Game
from human_vs_ai import *
from humanoid import Humanoid
from easy_ai import EasyAI
from ai import ImpossibleAI
from human_prompt_interface import HumanPromptInterface

class HumanoidVsAiScenario(HumanInvolvementBaseScenario):


    @staticmethod
    def name():
      return "Humanoid vs AI"

    def human_player(self, token):
      return Humanoid(token)

    @staticmethod
    def prompts():
      return HumanPromptInterface.prompts()
