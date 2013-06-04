import player

class AI(player.Player):

  def __init__(self,token):
      super(AI, self).__init__(token)

  def get_best_move(self,board_state):
      move_list = []
      for move in board_state.get_available_moves():
        move_score = self.get_best_move_score(move,board_state,self.token)
        move_list.append((move_score,move))
      move_list.sort()
      return move_list[-1][1]

  def cost_function(self, winner):
      cost_dict = {self.token:1, self.opponent_token:-1, None:0}
      return cost_dict[winner]

  def get_best_move_score(self, space, current_board, current_player,depth=0):
      try:
        current_board.make_move(space,current_player)
        possible_moves = current_board.get_available_moves()
        if depth == 4:
            return self.cost_function(current_board.winner())
        opposite_player = self.PLAYERS_DICT[current_player]
        move_scores = [self.get_best_move_score(move,current_board,opposite_player, depth+1) for move in possible_moves]
        if current_player == self.token:
            return min(move_scores)
        else:
            return max(move_scores)
      finally:
        current_board.erase_move(space)
