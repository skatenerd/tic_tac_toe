from __future__ import print_function
from player import Player
from board import Board
from ai import AI
from easy_ai import EasyAI
from playerinput import MoveValidator

class Game(object):

    def __init__(self,player_one,player_two,display_method="python_print"):
        self.gameboard = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.display_method = display_method.print_this if not display_method == "python_print" else print
    
    def run(self):
        self.__introduction__()
        while not self.__over__():
            self.__round_set__()
            self.__print_board_if_game_not_over__()
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
        self.display_method("Please select a move: ")
        self.__round__(self.player_one)
        self.__round__(self.player_two)

    def __round__(self,current_player):
            if not self.__over__():
                if not isinstance(current_player,AI):
                    self.display_method("Available moves are " + str(self.gameboard.available_moves()))
                    validator = MoveValidator()
                    move = validator.validate(current_player,self.gameboard.available_moves())
                else:
                    move = current_player.next_move(self.gameboard)
                self.__move__(move,current_player)

    def __print_board_if_game_not_over__(self):
        if not self.__over__():
            self.display_method(self.gameboard)

    def __over__(self):
        return self.gameboard.game_over()

    def __move__(self,space,player):
        self.gameboard.make_move(space,player.token)
