from playerinput import PlayerInput
from minimax import Minimax
from printer import Printer
from playerinput import InputValidator

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
	    move = self.__human_intervention__(board)
        else:
	    move =  Minimax(self.token,6).next_move(board)
	self.display_method(self.token.capitalize() + " moves to " + str(move))
	return move

    def __human_intervention__(self,board):
	self.display_method("Please select a move: ")
	self.display_method("Available moves are " + str(board.available_moves()))
        move = InputValidator.return_valid_response(self.input_object,board.available_moves())
        return move
