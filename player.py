class Player(object):

    PLAYERS_DICT = {'x':'o','o':'x'}

    def __init__(self,token):
      self.token = token
      self.opponent_token = (self.PLAYERS_DICT[token])


