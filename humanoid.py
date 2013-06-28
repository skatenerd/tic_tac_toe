from playerinput import PlayerInput
from minimax import Minimax
from printer import Printer

class Humanoid(object):

    def __init__(self,token,input_object=PlayerInput(),display_object=Printer()):
	self.token = token
        self.times_next_move_called = 0
        self.input_object = input_object
	self.display_method = display_object.display
 
    def next_move(self,board):
	self.display_method(self.token.capitalize() + "'s turn")
        self.times_next_move_called += 1 
        if self.times_next_move_called < 3:
            move = self.input_object.call() 
        else:
	    move =  Minimax(self.token,6).next_move(board)
	self.display_method(self.token.capitalize() + " moves to " + str(move))
	return move
