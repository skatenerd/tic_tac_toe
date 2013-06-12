import random
import sys
sys.path.append("../")
from player import Player
from board import Board

class MockUserInput(object):

    def __init__(self,vals):
        self.data = list(vals)
        self.times_called = 0

    def output(self):
        self.__increment_times_called__()
        print self.data
        return self.data.pop(0)

    def __increment_times_called__(self):
        self.times_called += 1

class MockPlayer(Player):

    def __init__(self,token,fake_input):
        super(MockPlayer,self).__init__(token,input_method=fake_input)

