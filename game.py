from board import Board
from ai import ImpossibleAI
from playerinput import MoveValidator
from printer import Printer
from easy_ai import EasyAI
from player import HumanPlayer
from humanoid import Humanoid

class Game(object):

    def __init__(self,player_one,player_two,display_object=Printer()):
        self.board = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.display_method = display_object.display
	self.current_player = player_one
    
    def run(self):
        self.__introduction__()
        while not self.__over__():
            self.__round_set__()
        self.display_method(self.board)
        self.__print_winner__()

    def __print_winner__(self):
        if self.board.winner():
            self.display_method(self.board.winner() + " wins")
        else:
            self.display_method("It's a tie.")

    def __introduction__(self):
        self.display_method(("\n1|2|3\n-------" +
                             "\n4|5|6\n-------" +
                             "\n7|8|9\n"))

    def __round_set__(self):
        self.__round__(self.player_one)
        self.__round__(self.player_two)

    def __round__(self,player):
            if not self.__over__():
		move = player.next_move(self.board)
                self.__move__(move,player)
		self.current_player = {self.player_one:self.player_two,
				       self.player_two:self.player_one}[self.current_player]
		self.__print_board_if_game_not_over__()

    def __print_board_if_game_not_over__(self):
        if not self.__over__():
            self.display_method(self.board)

    def __non_ai_move__(self,current_player):
        self.__print_board_if_game_not_over__()
        validator = MoveValidator()
        move = validator.validate(self.board,current_player,self.board.available_moves())
        return move	

    def __over__(self):
        return self.board.over()

    def __move__(self,space,player):
        self.board.make_move(space,player.token)
