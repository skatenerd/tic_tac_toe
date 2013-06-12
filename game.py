from __future__ import print_function
from player import Player
from board import Board
from ai import AI
from playerinput import InputValidator, PlayerInput

class Game(object):

    def __init__(self,player_one,player_two,display_method=print):
        self.gameboard = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.display_method = display_method
    
    def run(self):
        while not self.__over__():
            self.__round_set__()
            self.__print_board_if_game_not_over__()
        self.display_method(self.gameboard)

    def __setup__(self,input_source=PlayerInput()):
        validator = InputValidator(input_source)
        self.display_method("Would you like to go first or second (1,2): ")

    def __round_set__(self):
        self.__round__(self.player_one)
        self.__round__(self.player_two)

    def __round__(self,current_player):
        if not self.__over__():
            self.__move__(current_player.next_move(),current_player)

    def __print_board_if_game_not_over__(self):
        if not self.__over__():
            self.display_method(self.gameboard)

    def __over__(self):
        return self.gameboard.game_over()

    def __move__(self,space,player):
        self.gameboard.make_move(space,player.token)
