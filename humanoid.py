from playerinput import PlayerInput
from minimax import Minimax

class Humanoid(object):

    def __init__(self,token,input_object=PlayerInput()):
	self.token = token
        self.times_next_move_called = 0
        self.input_object = input_object
 
    def next_move(self,board):
        self.times_next_move_called += 1 
        if self.times_next_move_called < 3:
            return self.input_object.call() 
        else:
	    return Minimax(self.token,6).next_move(board)
