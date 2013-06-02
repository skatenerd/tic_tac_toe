# Version of Tic Tac Toe following TDD principles

class Board(object):

    def __init__(self):
        self.board_state = dict()

    def make_move(self, space, token):
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

    def winner(self):
        pass
