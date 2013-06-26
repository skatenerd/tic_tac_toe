from minimax import Minimax

class ImpossibleAI(object):

    def __init__(self,token):
	self.token = token

    def next_move(self,board):
	return Minimax(self.token,6).next_move(board)
