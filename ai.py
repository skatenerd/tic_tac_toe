from player import Player

class AI(Player):

  def __init__(self,token,difficulty="impossible"):
      super(AI, self).__init__(token)
      self.difficulty = difficulty

  def next_move(self,board):
      move_list = []
      possible_moves = board.available_moves()
      for move in possible_moves:
          move_score = self.__best_score__(move,board,self.token)
          move_list.append((move_score,move))
      if move_list:
          move = self.__select_move_based_on_difficulty__(move_list)
          return move

  def __select_move_based_on_difficulty__(self,move_list):
      if self.difficulty == "impossible":
          move = max(move_list)[-1]
      elif self.difficulty == "easy":
          move = min(move_list)[-1]
      return move

  def __best_score__(self, space, board, player, alpha=-1, beta=1):
      try:
          board.make_move(space,player)
          possible_moves = board.available_moves()
          if board.game_over():
              return self.__cost_function__(board.winner())
          next_player = self.PLAYERS_DICT[player]
          if self.__comp_turn__(player):
              for move in possible_moves:
                  beta = min(beta,self.__best_score__(move,board,next_player,alpha,beta))
                  if beta <= alpha:
                      break
              return beta
          else:
              for move in possible_moves:
                  alpha = max(alpha,self.__best_score__(move,board,next_player,alpha,beta))
                  if beta <= alpha:
                      break
              return alpha
      finally:
          board.erase_move(space)

  def __cost_function__(self, winner):
      cost_dict = {self.opponent_token:-1, self.token:1, None:0}
      return cost_dict[winner]

  def __comp_turn__(self, current_player):
      return current_player == self.token
