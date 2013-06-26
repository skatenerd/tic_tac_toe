from board import Board
from ai import ImpossibleAI
from playerinput import MoveValidator
from printer import Printer

class Game(object):

    def __init__(self,player_one,player_two,display_object=Printer()):
        self.gameboard = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.display_method = display_object.display
	self.current_player = player_one
    
    def run(self):
        self.__introduction__()
        while not self.__over__():
            self.__round_set__()
        self.display_method(self.gameboard)
        self.__print_winner__()

    def __print_winner__(self):
        if self.gameboard.winner():
            self.display_method(self.gameboard.winner() + " wins")
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
	        self.display_method(self.current_player.token.capitalize() + "'s turn")
		if not type(player) == ImpossibleAI:
		    move = self.__non_ai_move__(player)
                else:
		    move = player.next_move(self.gameboard)
                self.__move__(move,player)
		self.display_method(player.token + " moves to " + str(move))
		self.current_player = {self.player_one:self.player_two,
				       self.player_two:self.player_one}[self.current_player]
		self.__print_board_if_game_not_over__()

    def __print_board_if_game_not_over__(self):
        if not self.__over__():
            self.display_method(self.gameboard)

    def __non_ai_move__(self,current_player):
        self.display_method("Please select a move: ") 
        self.__print_board_if_game_not_over__()
	self.display_method("Available moves are " + str(self.gameboard.available_moves()))
        validator = MoveValidator()
        move = validator.validate(self.gameboard,current_player,self.gameboard.available_moves())
        return move	

    def __over__(self):
        return self.gameboard.game_over()

    def __move__(self,space,player):
        self.gameboard.make_move(space,player.token)
