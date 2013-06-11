from player import Player
from board import Board
from ai import AI

class Game(object):

    def __init__(self,player_one,player_two):
        self.gameboard = Board()
        self.player_one = player_one
        self.player_two = player_two

    def run(self):
        while not self.over():
            self.turn(self.player_one)
            if not self.over():
                self.turn(self.player_two)

    def turn(self,player):
        player_move = player.next_move(self.gameboard)
        self.move(player_move,player)
        print self.gameboard
        print player.token + " moves to " + str(player_move)
        print "\n_______________"

    def over(self):
        return self.gameboard.game_over()

    def move(self,space,player):
        self.gameboard.make_move(space,player.token)
