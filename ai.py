import player

class AI(player.Player):

  def __init__(self,token):
      super(AI, self).__init__(token)

  def next_move(self,board):
      move_list = []
      for move in board.available_moves():
          move_score = self.__best_score(move,board,self.token)
          move_list.append((move_score,move))
      if move_list:
          return max(move_list)[-1]

  #can you find a way to do this without mutating the board?
  #then you wouldn't have to worry about being Absolutely Sure that you "erase" the moves
  def __best_score(self, space, board, player, depth=0):
      try:
          board.make_move(space,player)
          possible_moves = board.available_moves()
          if board.game_over() or depth == 5:
              return self.__cost_function(board.winner())
          values = [self.__best_score(move,board,self.PLAYERS_DICT[player],depth+1) for move in possible_moves]
          if self.__comp_turn(player):
              return min(values)
          else:
              return max(values)
      finally:
          board.erase_move(space)

  def __cost_function(self, winner):
      cost_dict = {self.opponent_token:-1, self.token:1, None:0}
      return cost_dict[winner]

  def __comp_turn(self, current_player):
      return current_player == self.token
