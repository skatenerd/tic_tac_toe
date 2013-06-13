import player

class AI(player.Player):

  def __init__(self,token):
      super(AI, self).__init__(token)

  def next_move(self,board):
      move_list = []
      for move in board.available_moves():
          move_score = self.__best_score__(move,board,self.token)
          move_list.append((move_score,move))
      if move_list:
          return max(move_list)[-1]

  def __best_score__(self, space, board, player):
      try:
          new_board = board
          new_board.make_move(space,player)
          possible_moves = new_board.available_moves()
          if new_board.game_over():
              return self.__cost_function__(new_board.winner())
          next_player = self.PLAYERS_DICT[player]
          values = [self.__best_score__(move,new_board,next_player) for move in possible_moves]
          if self.__comp_turn__(player):
              return min(values)
          else:
              return max(values)
      finally:
          new_board.erase_move(space)

  def __cost_function__(self, winner):
      cost_dict = {self.opponent_token:-1, self.token:1, None:0}
      return cost_dict[winner]

  def __comp_turn__(self, current_player):
      return current_player == self.token