import unittest
from user_interface import *
from test_utils import *
from player import Player
from ai import AI
from easy_ai import EasyAI

class UserInterfaceGameSetupTests(unittest.TestCase):
    
    def test_if_game_setup_puts_players_in_proper_order(self):
        fake_printer = FakePrinter()
    	mock = MockUserInput([1,"o","easy"])
        ui = UserInterface(mock,fake_printer)
        game = ui.game_setup()
        self.assertTrue(isinstance(game.player_one,Player))

    def test_that_game_setup_prompts_player(self):
    	mock = MockUserInput([1,"o","easy"])
    	fake_printer = FakePrinter()
        ui = UserInterface(mock,fake_printer)
    	game = ui.game_setup()
    	self.assertEqual("Would you like to move first or second (1,2): ",fake_printer.history[0])

    def test_that_game_setup_validates_input_before_accepting(self):
    	mock = MockUserInput(["a",2,"x","easy"])
        ui = UserInterface(mock,FakePrinter())
    	game = ui.game_setup()
    	self.assertTrue(not isinstance(game.player_two,AI))

    def test_that_game_setup_prompts_player_at_least_twice(self):
    	mock = MockUserInput([2,"o","easy"])
    	fake_printer = FakePrinter()
        ui = UserInterface(mock,fake_printer)
    	ui.game_setup()
    	self.assertTrue(len(fake_printer.history) >= 2)

    def test_pick_token_returns_token(self):
        mock = MockUserInput([2,"o","easy"])
        ui = UserInterface(mock,FakePrinter())
        token = ui.pick_token()
        self.assertEqual("o",token)

    def test_game_setup_prompts_for_difficulty(self):
        mock = MockUserInput([2,"o","easy"])
        fake_printer = FakePrinter()
        ui = UserInterface(mock,fake_printer)
        ui.game_setup()
        self.assertTrue("Would like to play against an easy or impossible ai: " in fake_printer.history)

    def test_game_setup_returns_correct_objects(self):
        mock = MockUserInput([1,'x',"easy"])
        ui = UserInterface(mock)
        game = ui.game_setup()
        self.assertTrue("o",game.player_two.token)
        self.assertTrue(isinstance(game.player_two,EasyAI))

    def test_game_setup_prompts_scenario(self):
        mock = MockUserInput(['2','o','impossible'])
        fake_printer = FakePrinter() 
        ui = UserInterface(mock,fake_printer)
        prompt = ("Please choose a scenario: \n" +
                 "(1) Human vs AI\n" +
                 "(2) Human vs Human\n" +
                 "(3) AI vs AI\n"
                 "(4) Humanoid vs AI")
        ui.pick_scenario()
        history_string = " ".join(fake_printer.history) 
        self.assertTrue(prompt in history_string)

    
