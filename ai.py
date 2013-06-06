import player

class AI(player.Player):

  def __init__(self,token):
      super(AI, self).__init__(token)

  def best_move(self,board):
      move_list = []
      for move in board.available_moves():
          move_score = self.best_move_score(move,board,self.token)
          move_list.append((move_score,move))
      if move_list:
          move_list.sort()
          return max(move_list)[-1]

  def best_move_score(self, space, current_board, current_player):
      try:
        current_board.make_move(space,current_player)
        possible_moves = current_board.available_moves()
        if current_board.game_over():
            return self.cost_function(current_board.winner())
        opposite_player = self.PLAYERS_DICT[current_player]
        move_scores = [self.best_move_score(move,current_board,opposite_player) for move in possible_moves]
        if self.comp_turn(current_player):
          return min(move_scores)
        else:
          return max(move_scores)
      finally:
        current_board.erase_move(space)


  def cost_function(self, winner):
      cost_dict = {self.opponent_token:-1, self.token:1, None:0}
      return cost_dict[winner]


  def comp_turn(self, current_player):
      return current_player == self.token



