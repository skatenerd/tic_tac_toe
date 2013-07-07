from game import Game
from playerinput import InputValidator
from printer import Printer
from scenario_selector import ScenarioSelector
from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_human import HumanVsHumanScenario
from human_vs_ai import HumanVsAiScenario
from prompter import Prompter

class UserInterface(object):

    def __init__(self,user_input,display_object=Printer()):
      self.user_input = user_input
      self.display_object = display_object
      self.display_method = display_object.display

    def game_setup(self):
      scenario_number = self.pick_scenario()
      scenario_selector = ScenarioSelector(scenario_number)
      prompter = Prompter(self.display_object,self.user_input)
      prompter.prompt_and_collect_input(scenario_selector.scenario_prompts())
      user_responses = prompter.return_answer_hash()
      game = scenario_selector.return_game(user_responses)
      return game

