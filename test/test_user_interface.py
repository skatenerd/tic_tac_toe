import unittest
from user_interface import *
from test_utils import *
from player import Player
from ai import AI
from easy_ai import EasyAI
from humanoid_vs_ai import HumanoidVsAiScenario
from mock import Mock

class UserInterfaceGameSetupTests(unittest.TestCase):

    def test_if_game_setup_puts_players_in_proper_order(self):
	fake_user_input = [1,"o","easy",1]
	game = self.call_game_setup_with_input_list(fake_user_input)
        self.assertTrue(isinstance(game.player_one,Player))

    def test_pick_token_returns_token(self):
        mock = MockUserInput([2,"o","easy"])
        ui = UserInterface(mock,FakePrinter())
        token = ui.pick_token()
        self.assertEqual("o",token)

    def test_game_setup_for_prompts(self):
	prompt_one = ("Would like to play against an easy or impossible ai: ")
	prompt_two = ( "(1) Human vs AI\n" +
                 "(2) Human vs Human\n" +
                 "(3) AI vs AI\n" +
                 "(4) Humanoid vs AI")
        prompt_four = "Would you like to play as x or o: "
        prompt_three = "Would you like to move first or second (1,2): "
	self.test_for_prompts(prompt_one,prompt_two,prompt_three,prompt_four)

    def test_for_prompts(self,*prompts):
	dummy_input = [1,"x","easy",1]
	mock = MockUserInput(dummy_input)
        fake_printer = FakePrinter()
	ui = UserInterface(mock,fake_printer)
	ui.game_setup()
	history_string = " ".join(fake_printer.history)
	for prompt in prompts:
	    self.assertTrue(prompt in history_string)

    def call_game_setup_with_input_list(self,input_list):
	fake_printer = FakePrinter()
	mock = MockUserInput(input_list)
	ui = UserInterface(mock,fake_printer)
	return ui.game_setup()
