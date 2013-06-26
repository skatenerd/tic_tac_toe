from minimax import Minimax

class EasyAI(object):

    def __init__(self,token):
	self.token = token

    def next_move(self,board):
	return Minimax(self.token,1).next_move(board)
