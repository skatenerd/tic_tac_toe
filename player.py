import playerinput

class Player(object):

    PLAYERS_DICT = {'x':'o','o':'x'}

    def __init__(self,token,input_method=playerinput.PlayerInput()):
        self.token = token
        self.opponent_token = (self.PLAYERS_DICT[token])
        self.input_method = input_method

    def next_move(self,board):
        return self.input_method.output(board)