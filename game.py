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
            player_one_move = self.player_one.next_move(self.gameboard)
            self.move(player_one_move,self.player_one)
            print self.gameboard
            print self.player_one.token + " moves to " + str(player_one_move)
            print "\n_______________"
            if not self.over():
                player_two_move = self.player_two.next_move(self.gameboard)
                self.move(player_two_move,self.player_two)
                print self.player_two.token + " moves to " + str(player_two_move)
            print "\n_______________"
            print self.gameboard

    def over(self):
        return self.gameboard.game_over()

    def move(self,space,player):
        self.gameboard.make_move(space,player.token)
