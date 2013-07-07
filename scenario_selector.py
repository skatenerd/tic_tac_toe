from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from human_vs_human import HumanVsHumanScenario
from easy_vs_impossible_ai import EasyVsImpossibleAiScenario
from playerinput import InputValidator
from printer import *
from prompter import *
from collections import OrderedDict

class ScenarioSelector(object):

  scenario_list = {
      1: HumanVsAiScenario,
      2: HumanVsHumanScenario,
      3: AiVsAiScenario,
      4: HumanoidVsAiScenario
  }

  def __init__(self, user_input, printer = Printer()):
    self.user_input = user_input
    self.printer = printer
    self.prompter = Prompter(printer, user_input)

  def scenario_class(self):
    self.prompter.prompt_and_collect_input(OrderedDict({self.build_scenario_prompt(): [1,2,3,4]}))
    answer_hash = self.prompter.return_answer_hash()
    return ScenarioSelector.scenario_list[answer_hash.values()[0]]

  def build_scenario_prompt(self):
    to_join = ["Please choose a scenario:"]
    for (k,v) in ScenarioSelector.scenario_list.iteritems():
      to_join.append(self.string_for_entry(k,v))
    return "\n".join(to_join)

  def string_for_entry(self, k, v):
    return "(%s) %s" % (k, v.name())
