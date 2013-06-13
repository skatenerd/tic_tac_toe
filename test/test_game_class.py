import unittest
import sys
sys.path.append("../")
from game import *
from board import *
import sys
from test_utils import FakePrinter, MockUserInput, MockPlayer
from player import Player
from playerinput import InputValidator

class GameRunTests(unittest.TestCase):

    def test_that_player_one_moves(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5,6]))
        game = Game(fake_player_one,fake_player_two)
        game.run()
        times_game_prompts_player_one = fake_player_one.input_object.times_called
        self.assertTrue(times_game_prompts_player_one >= 1)

    def test_that_player_two_moves(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5,6]))
        game = Game(fake_player_one,fake_player_two)
        game.run()
        times_game_prompts_player_two = fake_player_two.input_object.times_called
        self.assertTrue(times_game_prompts_player_two >= 1)

    def test_that_players_dont_move_when_game_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        game = Game(fake_player_one,fake_player_two)
        for i in range(1,4):
            game.gameboard.make_move(i,"o")
        self.assertEqual(True,game.__over__())
        game.run()
        times_game_prompts_player_one = fake_player_one.input_object.times_called
        times_game_prompts_player_two = fake_player_two.input_object.times_called
        self.assertEqual(0,times_game_prompts_player_one)
        self.assertEqual(0,times_game_prompts_player_two)

    def test_that_board_is_printed_when_game_is_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2])) 
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer)
        for i in range(1,4):
            game.gameboard.make_move(i,"x")
        game.run()
        self.assertEqual(True,game.__over__())
        expected_string = ("\n%(1)3s|%(2)3s|%(3)3s\n------------" +
                           "\n%(4)3s|%(5)3s|%(6)3s\n------------" +
                           "\n%(7)3s|%(8)3s|%(9)3s") % game.gameboard.generate_layout()
        self.assertEqual(expected_string,fake_printer.last_print())

    def test_that_second_player_doesnt_move_when_game_is_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5,6]))
        game = Game(fake_player_one,fake_player_two)
        game.run()
        self.assertTrue(game.__over__())
        times_game_prompts_player_two = fake_player_two.input_object.times_called
        self.assertEqual(2,times_game_prompts_player_two)

    def test_that_game_prints_board_after_each_set_of_rounds(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer)
        game.run()
        # Two sets of rounds plus final print
        self.assertEqual(6,len(fake_printer.history))



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
        game = Game(fake_player_one,fake_player_two,fake_printer)
        game.__round_set__()
        self.assertEqual(1,len(fake_printer.history))

    def test_that_round_validates_user_input(self):
        fake_player_one = MockPlayer("x",MockUserInput(['a',2]))
        fake_player_two = MockPlayer("o",MockUserInput([3]))
        game = Game(fake_player_one,fake_player_two)
        game.__round__(fake_player_one)
        self.assertEqual({2:"x"},game.gameboard.state())

class GamePrintBoardIfNotOverTests(unittest.TestCase):

    def test_that_board_isnt_printed_when_game_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer)
        game.__print_board_if_game_not_over__()
        #Game gets printed once when game over
        self.assertEqual(1,len(fake_printer.history))

    def test_that_board_is_printed_when_game_not_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer)
        game.run()
        self.assertEqual(6,len(fake_printer.history))

class GameMoveTests(unittest.TestCase):

    def test_that_move_alters_state(self):
        user_input_one = MockUserInput([1])
        user_input_two = MockUserInput([2])
        player_one = MockPlayer("x",user_input_one)
        player_two = MockPlayer("o",user_input_two)
        game = Game(player_one,player_two)
        p_one_move = player_one.next_move(game.gameboard)
        game.__move__(p_one_move,player_one)
        p_two_move = player_two.next_move(game.gameboard)
        game.__move__(p_two_move,player_two)
        expected_state = {p_one_move:player_one.token,
                         p_two_move:player_two.token}
        actual_state = game.gameboard.state()
        self.assertEqual(expected_state,actual_state)