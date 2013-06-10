import random

class FakePlayerInput(object):

    def output(self,board):
        int_list = board.available_moves()
        return random.choice(int_list)


class PlayerInput(object):

    def output(self,board):
        available_moves = board.available_moves()
        space = 0
        while space not in available_moves:
            print available_moves
            space = int(raw_input("Where would you like to move: "))
        return space
