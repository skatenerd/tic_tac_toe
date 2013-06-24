from ai import AI
from player import Player
from playerinput import PlayerInput

class Humanoid(AI):

    def __init__(self,token,input_object=PlayerInput()):
        super(AI,Humanoid).__init__(self,token,input_object)
        self.times_next_move_called = 0
        self.input_object = input_object
	self.minimax_status = {"alpha":-1,"beta":1}
	self.depth = 1
	self.MAX_DEPTH = 2500
 
    def next_move(self,board):
        self.times_next_move_called += 1 
        if self.times_next_move_called < 3:
            return self.input_object.call() 
        else:
            return AI.next_move(self,board) 
