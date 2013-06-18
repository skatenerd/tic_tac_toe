from player import Player

class AI(Player):

  def __init__(self,token):
      super(AI, self).__init__(token)
      self.minimax_status = {"alpha":-1,"beta":1}

  def next_move(self,board):
      move_list = self.__build_move_list__(board)
      if move_list:
          best_move = max(move_list)[-1]
          return best_move

  def __build_move_list__(self,board):
      move_list = []
      possible_moves = board.available_moves()
      for move in possible_moves:
          move_score = self.__best_score__(move,board,self.token)
          move_list.append((move_score,move))
      return move_list

  def __best_score__(self, space, board, player):
      try:
          board.make_move(space,player)
          if board.game_over():
              return self.__cost_function__(board.winner())
          return self.__alpha_beta_prune__(board, player)
      finally:
          board.erase_move(space)

  def __alpha_beta_prune__(self, board, player):
      next_player = self.PLAYERS_DICT[player]
      if self.__comp_turn__(player):
          return self.__return_beta__(board,next_player)
      else:
          return self.__return_alpha__(board,next_player)

  def __return_beta__(self,board,next_player):
      beta = self.minimax_status["beta"] 
      alpha = self.minimax_status["alpha"]
      possible_moves = board.available_moves()
      for move in possible_moves:
          beta = min(beta, self.__best_score__(move,board,next_player))
          if beta <= alpha:
              break
      return beta

  def __return_alpha__(self,board,next_player):
      alpha = self.minimax_status["alpha"]
      beta = self.minimax_status["beta"]
      possible_moves = board.available_moves()
      for move in possible_moves:
          alpha = max(alpha,self.__best_score__(move,board,next_player))
          if beta <= alpha:
              break
      return alpha

  def __cost_function__(self, winner):
      cost_dict = {self.opponent_token:-1, self.token:1, None:0}
      return cost_dict[winner]

  def __comp_turn__(self, current_player):
      return current_player == self.token