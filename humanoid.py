from ai import AI
from player import Player

class Humanoid(AI):

    def __init__(self,token,input_object):
        super(AI,Humanoid).__init__(self,token,input_object)
        self.times_next_move_called = 0
        self.minimax_status = {"alpha":-1,"beta":1}
 
    def next_move(self,board):
        self.times_next_move_called += 1 
        if self.input_object and self.times_next_move_called < 4:
            return self.input_object.call() 
        return AI.next_move(self,board) 
