from game import Game
from playerinput import InputValidator
from printer import Printer
from scenario_selector import ScenarioSelector
from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_human import HumanVsHumanScenario
from human_vs_ai import HumanVsAiScenario
from prompter import Prompter

class GameFactory(object):
  def __init__(self, scenario_class, prompter):
    self.scenario_class = scenario_class
    self.prompter = prompter

  def game(self):
    self.prompter.prompt_and_collect_input(self.scenario_class.prompts())
    scenario = self.scenario_class(self.prompter.return_answer_hash())
    return scenario.game()

class UserInterface(object):

    def __init__(self,user_input,display_object=Printer()):
      self.user_input = user_input
      self.display_object = display_object
      self.display_method = display_object.display

    def game_setup(self):
      scenario_selector = ScenarioSelector(self.user_input, self.display_object)
      scenario_class = scenario_selector.scenario_class()
      prompter = Prompter(self.display_object,self.user_input)
      game = GameFactory(scenario_class, prompter).game()
      return game

