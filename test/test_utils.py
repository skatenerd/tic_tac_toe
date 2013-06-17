import random
import sys
sys.path.append("../")
from player import Player
from board import Board

class MockUserInput(object):

    def __init__(self,vals):
        self.data = list(vals)
        self.times_called = 0

    def call(self):
        self.__increment_times_called__()
        return self.data.pop(0)

    def __increment_times_called__(self):
        self.times_called += 1

class ScriptedPlayer(Player):

    def __init__(self,token,moves):
        self.token = token
        self.moves = moves
        self.times_called = 0

    def next_move(self,board):
        self.times_called += 1
        return self.moves.pop(0)

class MockPlayer(Player):

    def __init__(self,token,fake_input):
        super(MockPlayer,self).__init__(token,fake_input)

class FakePrinter(object):

    def __init__(self):
        self.history = []

    def print_this(self,item):
        self.history.append(item.__str__())
        print item

    def last_print(self):
        try:
            return self.history.pop()
        except IndexError:
            print "history must be populated."
            return []
