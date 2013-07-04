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
      scenario = scenario_selector.return_scenario(user_responses)
      if type(scenario) == Game:
        return scenario
      else:
        return scenario.setup()

    def pick_scenario(self):
      prompt = self.build_scenario_prompt()
      scenario = self.__prompt_loop__(prompt,(1,2,3,4))
      return scenario

    def build_scenario_prompt(self):
      to_join = ["Please choose a scenario: \n"]
      for (k,v) in ScenarioSelector.scenario_list.iteritems():
        to_join.append(self.string_for_entry(k,v))
      return "\n".join(to_join)

    def string_for_entry(self, k, v):
      return "(%s) %s" % (k, v.name())

    def __prompt_loop__(self,prompt,valid_responses):
        self.display_method(prompt)
        validator = InputValidator()
        response = validator.return_valid_response(self.user_input, (valid_responses))
        return response
