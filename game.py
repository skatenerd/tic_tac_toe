from __future__ import print_function
from player import Player
from board import Board
from ai import AI

class Game(object):

    def __init__(self,player_one,player_two,display_method=print):
        self.gameboard = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.display_method = display_method

    def run(self):
        self.display_method(self.gameboard)

    def __over__(self):
        return self.gameboard.game_over()

    def __move__(self,space,player):
        self.gameboard.make_move(space,player.token)
