import unittest
from tic_tac_toe import *
from test_utils import *
from player import Player

class TicTacToeCreateGameTests(unittest.TestCase):
    
    def test_if_game_setup_puts_players_in_proper_order(self):
    	mock = MockUserInput([1])
        game = game_setup(mock)
        self.assertTrue(isinstance(game.player_one,Player))

    def test_that_game_setup_prompts_player(self):
    	mock = MockUserInput([1])
    	fake_printer = FakePrinter()
    	game = game_setup(mock,display_object=fake_printer)
    	self.assertEqual("Would you like to move first or second: ",fake_printer.history[0])

    def test_that_game_setup_validates_input_before_accepting(self):
    	mock = MockUserInput(["a",2])
    	game = game_setup(mock)
    	self.assertTrue(not isinstance(game.player_two,AI))

    def test_that_game_setup_prompts_player_twice(self):
    	mock = MockUserInput([2])
    	fake_printer = FakePrinter()
    	game = game_setup(mock,display_object=fake_printer)
    	self.assertEqual(2,len(fake_printer.history))

         