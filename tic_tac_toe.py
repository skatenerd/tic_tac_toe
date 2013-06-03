# Version of Tic Tac Toe following TDD principles

class Board(object):

    WINNING_COMBOS = [[1,2,3],[4,5,6],[7,8,9],
                      [1,4,7],[2,5,8],[3,6,9],
                      [1,5,9], [3,5,7]]


    def __init__(self):
        self.board_state = dict()

    def make_move(self, space, token):
        if space in self.get_available_moves():
            self.board_state[space] = token

    def is_full(self):
        occupied_spaces = self.board_state.keys()
        if occupied_spaces == range(1,10):
            return True
        return False

    def get_available_moves(self):
        spaces_taken = self.board_state.keys()
        move_list = range(1,10)
        available_moves = [move for move in move_list if move not in spaces_taken]
        return available_moves

    def pieces_match(self,combo):
        occupied_spaces = self.board_state.keys()
        if combo[0] in occupied_spaces and combo[1] in occupied_spaces and combo[2] in occupied_spaces:
            first_piece = self.board_state[combo[0]]
            second_piece = self.board_state[combo[1]]
            third_piece = self.board_state[combo[2]]
            return first_piece == second_piece == third_piece
        return False

    def winner(self):
        for combo in self.WINNING_COMBOS:
            if self.pieces_match(combo):
                return self.board_state[combo[0]]
        return None

    def game_over(self):
        if self.is_full() or self.winner():
            return True
        return False

    def erase_move(self,move):
        del self.board_state[move]

class Player(object):

    PLAYERS_DICT = {'x':'o','o':'x'}

    def __init__(self,token):
      self.token = token
      self.opponent_token = self.PLAYERS_DICT[token]

class AI(Player):

  def __init__(self,token):
      super(AI, self).__init__(token)

  def cost_function(self, winner):
      cost_dict = {self.token:1, self.opponent_token:-1, None:0}
      return cost_dict[winner]

  def get_best_move_score(self, space, current_board, current_player):
      try:
        current_board.make_move(space,current_player)
        possible_moves = current_board.get_available_moves()
        if current_board.game_over():
            return self.cost_function(current_board.winner())
        opposite_player = self.PLAYERS_DICT[current_player]
        move_scores = [self.get_best_move_score(move,current_board,opposite_player) for move in possible_moves]
        if current_player == self.token:
            return min(move_scores)
        else:
            return max(move_scores)
      finally:
        current_board.erase_move(space)

  def get_best_move(self,current_game_board):
    possible_moves = current_game_board.get_available_moves()
    move_list_hash = {}
    move_list = []
    for move in possible_moves:
      move_score = self.get_best_move_score(move,current_game_board,self.token)
      move_list_hash[move_score] = move
    print move_list_hash.keys()
    return move_list_hash[move_list[0]]
