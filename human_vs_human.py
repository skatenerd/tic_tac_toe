from player import HumanPlayer
from game import Game
from no_prompt_interface import NoPromptInterface

class HumanVsHumanScenario(object):
    @staticmethod
    def name():
      return "Human vs Human"

    def __init__(self, user_data):
      pass

    def game(self):
      player_one = HumanPlayer("x")
      player_two = HumanPlayer("o")
      return Game(player_one,player_two)

    @staticmethod
    def prompts():
      return NoPromptInterface.prompts()
