import unittest
from game import *
from board import *
from test_utils import FakePrinter, MockUserInput, MockPlayer, ScriptedPlayer
from player import Player
from playerinput import InputValidator

class GameRunTests(unittest.TestCase):

    def assertInputObjectsCalled(self,input_obj_one,input_obj_two):
	self.assertTrue(input_obj_one.times_called >= 1 and
			input_obj_two.times_called >= 1)

    def assertInputObjectsNotCalled(self,input_obj_one,input_obj_two):
	self.assertTrue(input_obj_one.times_called == 0 and
			input_obj_two.times_called == 0)

    def create_fake_players(self,*input_objs):
	input_object_one,input_object_two = input_objs
	player_one = MockPlayer("x",input_object_one)
	player_two = MockPlayer("o",input_object_two)
	return player_one, player_two
    
    def create_fake_input_objects(self,input_list_one,input_list_two):
	input_one = MockUserInput(input_list_one)
	input_two = MockUserInput(input_list_two)
	return input_one, input_two

    def test_that_players_move(self):
	player_one_input,player_two_input = self.create_fake_input_objects([1,2,3],[4,5,6])
	fake_player_one,fake_player_two = self.create_fake_players(player_one_input,player_two_input)
	game = Game(fake_player_one, fake_player_two)
	game.run()
	self.assertInputObjectsCalled(player_one_input,player_two_input)

    def test_that_players_dont_move_when_game_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        game = Game(fake_player_one,fake_player_two)
	game.gameboard.board_state = {1:"x",2:"o",3:"x",
			              4:"o",5:"x",6:"o",
				      7:"x",8:"o",9:"x"}
        self.assertEqual(True,game.__over__())
        game.run()
	self.assertInputObjectsNotCalled(fake_player_one.input_object,
			                 fake_player_two.input_object)

    def test_that_board_is_printed_when_game_is_over(self):
	fake_player_one = MockPlayer("x",MockUserInput([1]))
	fake_player_two = MockPlayer("o",MockUserInput([2]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
	game.gameboard.board_state = {1:"x",2:"x",3:"x"}
        game.run()
        self.assertEqual(True,game.__over__())
        expected_string = ("\n%(1)3s|%(2)3s|%(3)3s\n------------" +
                           "\n%(4)3s|%(5)3s|%(6)3s\n------------" +
                           "\n%(7)3s|%(8)3s|%(9)3s") % game.gameboard.generate_layout()
        self.assertTrue(expected_string in fake_printer.history)

    def test_that_game_prints_board_after_each_set_of_rounds(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        # Two sets of rounds plus final print
        self.assertTrue(len(fake_printer.history) >= 6)

    def test_that_game_displays_winner(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        self.assertEqual("x",game.gameboard.winner())
        self.assertTrue("x wins" in fake_printer.history)

    def test_that_game_prints_tie(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,6,8,7,5]))
        fake_player_two = MockPlayer("o",MockUserInput([2,3,4,9]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        self.assertEqual(None,game.gameboard.winner())
        self.assertTrue("It's a tie." in fake_printer.history)

    def test_for_move_announcements(self):
	fake_player_one = MockPlayer("x",MockUserInput([1]))
	fake_player_two = MockPlayer("o",MockUserInput([2]))
	fake_printer = FakePrinter()
	game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
	game.gameboard.board_state = {2:"x",3:"x"}
	game.run()
	self.assertTrue("x moves to 1" in fake_printer.history)

    def test_that_current_player_var_alternates(self):
        input_one,input_two = self.create_fake_input_objects([1,2,3],[4,5,6])
	player_one,player_two = self.create_fake_players(input_one,input_two)
        game = Game(player_one,player_two)
	#First player is x
	self.assertEqual("x",game.current_player.token)
	game.run()
	self.assertEqual("o",game.current_player.token)

class GameRoundTests(unittest.TestCase):

    def test_that_round_doesnt_run_when_game_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4]))
        game = Game(fake_player_one,fake_player_two)
        for i in range(1,4):
            game.gameboard.make_move(i,"o")
        self.assertTrue(game.__over__())
        game.__round__(fake_player_one)
        times_game_prompts_player_one = fake_player_one.input_object.times_called
        self.assertEqual(0,times_game_prompts_player_one)

    def test_that_round_shows_available_moves(self):
        fake_player_one = MockPlayer("x", MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.__round__(fake_player_one)
        expected_string = ("Available moves are ")
        NOT_FOUND = -1
        history_string = " ".join(fake_printer.history) 
        status = history_string.find(expected_string) 
        self.assertTrue(status != NOT_FOUND)
 
    def test_that_round_set_calls_each_player(self):
        fake_player_one_input = MockUserInput([1])
        fake_player_two_input = MockUserInput([2])
        fake_player_one = MockPlayer("o",fake_player_one_input)
        fake_player_two = MockPlayer("x",fake_player_two_input)
        game = Game(fake_player_one,fake_player_two)
        game.__round_set__()
        times_game_prompts_player_one = fake_player_one_input.times_called
        times_game_prompts_player_two = fake_player_two_input.times_called
        self.assertEqual(1,times_game_prompts_player_one)
        self.assertEqual(1,times_game_prompts_player_two)

    def test_that_round_set_prompts_player(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        fake_printer = FakePrinter()
        prompt = "Please select a move: "
        game = Game(fake_player_one,fake_player_two,fake_printer)
        game.__round_set__()
        self.assertTrue(prompt in fake_printer.history)

    def test_that_round_validates_user_input(self):
        fake_player_one = MockPlayer("x",MockUserInput(['a',2]))
        fake_player_two = MockPlayer("o",MockUserInput([3]))
        game = Game(fake_player_one,fake_player_two)
        game.__round__(fake_player_one)
        self.assertEqual({2:"x"},game.gameboard.state())
   
    def test_that_board_is_shown_during_human_round_only(self):
        computer = AI("o")
        fake_human = MockPlayer("x",MockUserInput([1,2]))
        fake_printer = FakePrinter() 
        game = Game(computer,fake_human,fake_printer)
        history_string = " ".join(fake_printer.history) 
        game.__round__(computer)
        board_printed = game.gameboard.__str__() in history_string 
        self.assertTrue(not board_printed)   
        board_before_human_move = game.gameboard.__str__() 
        game.__round__(fake_human)
        new_history_string = " ".join(fake_printer.history) 
        self.assertTrue(board_before_human_move in new_history_string)
 
    def test_that_sample_board_shown(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        example_board = ("\n1|2|3\n-------" +
                          "\n4|5|6\n-------" +
                          "\n7|8|9\n")
        self.assertTrue(example_board in fake_printer.history)


class GamePrintBoardIfNotOverTests(unittest.TestCase):

    def test_that_board_isnt_printed_when_game_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.__print_board_if_game_not_over__()
        #Game gets printed once when game over
        self.assertEqual(1,len(fake_printer.history))

    def test_that_board_is_printed_when_game_not_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        self.assertTrue(len(fake_printer.history) >= 6)

class GameMoveTests(unittest.TestCase):

    def test_that_move_works_with_easy_ai(self):
        computer = EasyAI("o")
        game = Game(Player("x"),computer)
        game.__move__(computer.next_move(game.gameboard),computer)
        empty_board = {}
        self.assertTrue(game.gameboard.state() != empty_board)
