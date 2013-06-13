import unittest
import sys
sys.path.append("../")
from game import *
from board import *
import sys
from test_utils import MockUserInput, MockPlayer
from player import Player
from playerinput import InputValidator

class GameRunTests(unittest.TestCase):

    def test_that_player_one_moves(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5,6]))
        game = Game(fake_player_one,fake_player_two)
        game.run()
        #it took me a minute to realize that "fake_player_one.input_method" refers to the mock input "MockUserInput([1,2,3])"
        #you are talking about input_method when really you are desciribng a conversation between player and game.  try to make this more expressive
        self.assertTrue(fake_player_one.input_method.times_called >= 1)

    def test_that_player_two_moves(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5,6]))
        game = Game(fake_player_one,fake_player_two)
        game.run()
        self.assertTrue(fake_player_two.input_method.times_called >= 1)

    def test_that_players_dont_move_when_game_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        game = Game(fake_player_one,fake_player_two)
        for i in range(1,4):
            game.gameboard.make_move(i,"o")
        self.assertEqual(True,game.__over__())
        game.run()
        self.assertEqual(0,fake_player_one.input_method.times_called)
        self.assertEqual(0,fake_player_two.input_method.times_called)

    def test_that_board_is_printed_when_game_is_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer.print_this)
        for i in range(1,4):
            game.gameboard.make_move(i,"x")
        game.run()
        self.assertEqual(True,game.__over__())
        #you're asserting that a string gets printed, but not what it is?
        self.assertEqual(str,type(fake_printer.last_print()))

    def test_that_second_player_doesnt_move_when_game_is_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5,6]))
        game = Game(fake_player_one,fake_player_two)
        game.run()
        self.assertTrue(game.__over__())
        self.assertEqual(2,fake_player_two.input_method.times_called)

    def test_that_game_prints_board_after_each_set_of_rounds(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer.print_this)
        game.run()
        # Two sets of rounds plus final print
        self.assertEqual(3,len(fake_printer.history))
        #why not pass in the fake_printer, instead of a method?
        #it was unclear to me that there was a mock object, coupled to the "print_this" method,
        #whose state changes with every call



class GameRoundTests(unittest.TestCase):

    def test_that_round_doesnt_run_when_game_over(self):
        fake_player = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4]))
        game = Game(fake_player,fake_player_two)
        for i in range(1,4):
            game.gameboard.make_move(i,"o")
        self.assertTrue(game.__over__())
        game.__round__(fake_player)
        self.assertEqual(0,fake_player.input_method.times_called)

    def test_that_round_set_calls_each_player(self):
      #how are these tests different from the ones above?
      #do you think that the run() tests provide a complete specification on their own?
        fake_player_one_input = MockUserInput([1])
        fake_player_two_input = MockUserInput([2])
        fake_player_one = MockPlayer("o",fake_player_one_input)
        fake_player_two = MockPlayer("x",fake_player_two_input)
        game = Game(fake_player_one,fake_player_two)
        game.__round_set__()
        self.assertEqual(1,fake_player_one_input.times_called)
        self.assertEqual(1,fake_player_two_input.times_called)

class GamePrintBoardIfNotOverTests(unittest.TestCase):

    def test_that_board_isnt_printed_when_game_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer.print_this)
        game.__print_board_if_game_not_over__()
        #Game gets printed once when game over
        self.assertEqual(1,len(fake_printer.history))

    def test_that_board_is_printed_when_game_not_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer.print_this)
        game.run()
        self.assertEqual(3,len(fake_printer.history))

class GameMoveTests(unittest.TestCase):

    def test_that_move_alters_state(self):
        user_input_one = MockUserInput([1])
        user_input_two = MockUserInput([2])
        player_one = MockPlayer("x",user_input_one)
        player_two = MockPlayer("o",user_input_two)
        game = Game(player_one,player_two)
        p_one_move = player_one.next_move()
        game.__move__(p_one_move,player_one)
        p_two_move = player_two.next_move()
        game.__move__(p_two_move,player_two)
        expected_state = {p_one_move:player_one.token,
                         p_two_move:player_two.token}
        actual_state = game.gameboard.state()
        self.assertEqual(expected_state,actual_state)

class GameSetupTests(unittest.TestCase):

    def test_that_setup_prompts_player(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([3]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer.print_this)
        game.__setup__(MockUserInput([2]))
        #can you find a way to be more specific about the contents?
        self.assertEqual(1,len(fake_printer.history))

    def test_that_setup_validates_input(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([3]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_method=fake_printer.print_this)
        game.__setup__(MockUserInput(['a','b',2]))
        self.assertEqual(1,len(fake_printer.history))
        self.assertIsInstance(game.player_two,Player)


#some of the mocks live in test files and others live in test_utils.py.  it would be easier to find them if it was consistent.
class FakePrinter(object):

    def __init__(self):
        self.history = []

    def print_this(self,item):
        self.history.append(item.__str__())
        print item

    def last_print(self):
        return self.history.pop()

