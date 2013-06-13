from __future__ import print_function
from player import Player
from board import Board
from ai import AI
from playerinput import InputValidator, PlayerInput

class Game(object):

    def __init__(self,player_one,player_two,display_method="python_print"):
        self.gameboard = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.display_method = display_method.print_this if not display_method == "python_print" else print
    
    def run(self):
        while not self.__over__():
            self.__round_set__()
            self.__print_board_if_game_not_over__()
        self.display_method(self.gameboard)

    def __round_set__(self):
        self.display_method("Please select a move: ")
        self.__round__(self.player_one)
        self.__round__(self.player_two)

    def __round__(self,current_player):
            if not self.__over__():
                if not isinstance(current_player,AI):
                    validator = InputValidator()
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
