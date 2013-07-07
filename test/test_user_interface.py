import unittest
from user_interface import *
from test_utils import *

the_user_input = {"age" : 5}

class MockScenario(object):
  @staticmethod
  def prompts():
    return {"age" : [1,2,3,4,5,6,7,8,9,10]}

  def __init__(self, user_input):
    self.user_input = user_input

  def game(self):
    if self.user_input == the_user_input:
      return "the game"
    else:
      return None

class MockPrompter(object):
  def __init__(self, to_return):
    self.to_return = to_return
    self.history = []
  def prompt_and_collect_input(self, prompts):
    self.history.append(prompts)
  def return_answer_hash(self):
    return self.to_return


class GameFactoryTests(unittest.TestCase):
  def test_builds_game(self):
    prompter = MockPrompter(the_user_input)
    factory = GameFactory(MockScenario, prompter)
    game = factory.game()
    self.assertEqual(game, "the game")

  def test_uses_scenario_prompts(self):
    prompter = MockPrompter(the_user_input)
    factory = GameFactory(MockScenario, prompter)
    game = factory.game()
    self.assertEqual(prompter.history, [{'age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}])


class UserInterfaceGameSetupTests(unittest.TestCase):
  pass
#    def call_game_setup_with_input_list(self,input_list):
#      fake_printer = FakePrinter()
#      mock = MockUserInput(input_list)
#      ui = UserInterface(mock,fake_printer)
#      return ui.game_setup()
#
#class UserInterfaceShowFlaggedPromptsTests(unittest.TestCase):
#
#    def test_that_only_flagged_prompts_are_shown(self):
#      mock = MockUserInput([3,"easy"])
#      fake_printer = FakePrinter()
#      ui = UserInterface(mock,fake_printer)
#      ui.game_setup()
#      # Prompt for choosing scenario is only necessary prompt
#      prompts_necessary_for_scenario_three = 2
#      printed_strings = len(fake_printer.history)
#      self.assertEqual(printed_strings,prompts_necessary_for_scenario_three)
#
#      mock = MockUserInput([2])
#      fake_printer = FakePrinter()
#      ui = UserInterface(mock,fake_printer)
#      ui.game_setup()
#      prompts_necessary_for_scenario_two = 1
#      printed_strings = len(fake_printer.history)
#      self.assertEqual(printed_strings,prompts_necessary_for_scenario_two)
#
#
