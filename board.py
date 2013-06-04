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
