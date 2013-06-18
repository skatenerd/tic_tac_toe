import playerinput

class Player(object):

    PLAYERS_DICT = {'x':'o','o':'x'}

    def __init__(self,token,input_object=playerinput.PlayerInput()):
        self.token = token
        self.opponent_token = (self.PLAYERS_DICT[token])
        self.input_object = input_object

    def next_move(self,board=None):
        return self.input_object.call()

