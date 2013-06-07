import player

class AI(player.Player):

  def __init__(self,token):
      super(AI, self).__init__(token)

  def best_move(self,board):
      move_list = []
      for move in board.available_moves():
          move_score = self.best_score(move,board,self.token)
          move_list.append((move_score,move))
      if move_list:
          move_list.sort()
          return max(move_list)[-1]

  def best_score(self, space, board, player):
      try:
          board.make_move(space,player)
          possible_moves = board.available_moves()
          if board.game_over():
              return self.cost_function(board.winner())
          else:
              values = []
              for move in possible_moves:
                  values.append(self.best_score(move,board,self.PLAYERS_DICT[player]))
              if player == self.token:
                  return min(values)
              else:
                  return max(values)
      finally:
          board.erase_move(space)

  def cost_function(self, winner):
      cost_dict = {self.opponent_token:-1, self.token:1, None:0}
      return cost_dict[winner]

  def comp_turn(self, current_player):
      return current_player == self.token



